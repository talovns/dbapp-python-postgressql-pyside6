from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDate
from PySide6.QtGui import QStandardItemModel, QStandardItem
from .ui.ui_report_dialog import Ui_ReportDialog      # ← сгенерированный класс
from . import db

class ReportDialog(QDialog, Ui_ReportDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setShowGrid(True)

        # предзаполнение фильтров
        self.fromDate.setCalendarPopup(True)
        self.toDate.setCalendarPopup(True)
        self.fromDate.setDate(QDate.currentDate().addMonths(-1))
        self.toDate.setDate(QDate.currentDate())
        if self.categoryCombo.count() == 0:
            self.categoryCombo.addItems(["(все)","Food","Transport","Entertainment","Health","Education","Utilities","Other"])

        self.applyBtn.clicked.connect(self.refresh)
        self.refresh()

    def refresh(self):
        username = 'demo'
        fdate = self.fromDate.date().toString("yyyy-MM-dd")
        tdate = self.toDate.date().toString("yyyy-MM-dd")
        cat = None if self.categoryCombo.currentIndex() == 0 else self.categoryCombo.currentText()
        q = self.queryEdit.text().strip() or None

        sql = """
        SELECT e.spent_at, e.amount, e.category, e.method,
               COALESCE(m.name,'—') AS merchant, e.note
        FROM expense e
        LEFT JOIN merchant m ON m.merchant_id = e.merchant_id
        WHERE e.user_id = (SELECT user_id FROM app_user WHERE username=%s)
          AND (%s::date IS NULL OR e.spent_at >= %s::date)
          AND (%s::date IS NULL OR e.spent_at <= %s::date)
          AND (%s::expense_category IS NULL OR e.category = %s::expense_category)
          AND (%s IS NULL OR e.note ILIKE '%%'||%s||'%%' OR m.name ILIKE '%%'||%s||'%%')
        ORDER BY e.spent_at DESC, e.created_at DESC;
        """
        rows = db.fetchall(sql, [username, fdate, fdate, tdate, tdate, cat, cat, q, q, q])

        model = QStandardItemModel(0, 6)
        model.setHorizontalHeaderLabels(["Дата","Сумма","Категория","Оплата","Магазин","Заметка"])
        for r in rows:
            items = [
                QStandardItem(str(r["spent_at"])),
                QStandardItem(f'{r["amount"]}'),
                QStandardItem(r["category"]),
                QStandardItem(r["method"]),
                QStandardItem(r["merchant"]),
                QStandardItem(r["note"] or "")
            ]
            for it in items:
                it.setEditable(False)
            model.appendRow(items)

        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()
        self.tableView.horizontalHeader().setStretchLastSection(True)
