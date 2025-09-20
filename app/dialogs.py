import logging
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QDate

from .ui.ui_add_expense import Ui_AddExpenseDialog  # под твой способ загрузки
from . import db
from .audit import log_action

log = logging.getLogger(__name__)

class AddExpenseDialog(QDialog, Ui_AddExpenseDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())
        if self.categoryCombo.count() == 0:
            self.categoryCombo.addItems(["Food","Transport","Entertainment","Health","Education","Utilities","Other"])
        if self.methodCombo.count() == 0:
            self.methodCombo.addItems(["Cash","Card","Online"])

        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.reject)

    def save(self):
        log_action("add_expense_submit_click")
        try:
            amount = float(self.amountEdit.text().replace(",", "."))
            if amount <= 0:
                raise ValueError("Сумма должна быть > 0")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка ввода", str(e))
            log_action("add_expense_validated", ok=False, error=str(e))
            return

        merchant_name = self.merchantEdit.text().strip() or None
        merchant_id = None
        if merchant_name:
            sql = """
            INSERT INTO merchant(name) VALUES(%s)
            ON CONFLICT(name) DO UPDATE SET name=EXCLUDED.name
            RETURNING merchant_id;
            """
            merchant_id = db.fetchall(sql, [merchant_name])[0]["merchant_id"]

        sql = """
        INSERT INTO expense(user_id, merchant_id, category, method, amount, spent_at, note)
        VALUES (
          (SELECT user_id FROM app_user WHERE username='demo'),
          %s, %s::expense_category, %s::payment_method, %s, %s::date, NULLIF(%s,'')
        );
        """
        params = [
            merchant_id,
            self.categoryCombo.currentText(),
            self.methodCombo.currentText(),
            amount,
            self.dateEdit.date().toString("yyyy-MM-dd"),
            self.noteEdit.text()
        ]
        try:
            db.execute(sql, params)
            log_action("add_expense_saved", ok=True,
                       amount=amount,
                       category=self.categoryCombo.currentText(),
                       method=self.methodCombo.currentText(),
                       merchant=merchant_name)
            self.accept()
        except Exception as e:
            log.exception("add_expense save failed")
            log_action("add_expense_saved", ok=False, error=str(e))
            QMessageBox.critical(self, "Ошибка записи", str(e))
