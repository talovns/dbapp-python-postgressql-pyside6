from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtCore import QDate
from .ui.ui_add_expense import Ui_AddExpenseDialog   # ← сгенерированный класс
from . import db

class AddExpenseDialog(QDialog, Ui_AddExpenseDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # предзаполнение
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())
        if self.categoryCombo.count() == 0:
            self.categoryCombo.addItems(["Food","Transport","Entertainment","Health","Education","Utilities","Other"])
        if self.methodCombo.count() == 0:
            self.methodCombo.addItems(["Cash","Card","Online"])

        # кнопки Ok/Cancel
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.reject)

    def save(self):
        # валидация
        try:
            amount = float(self.amountEdit.text().replace(",", "."))
            if amount <= 0:
                raise ValueError("Сумма должна быть > 0")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка ввода", str(e))
            return

        # upsert магазина и вставка расхода
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
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка записи", str(e))
