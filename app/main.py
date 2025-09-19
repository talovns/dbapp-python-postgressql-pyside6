import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from .ui.ui_mainwindow import Ui_MainWindow              # ← добавили
from .logging_conf import setup_logging
from . import db
from .dialogs import AddExpenseDialog
from .views import ReportDialog                          # ← будем вызывать диалог отчёта

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # ← создаёт виджеты из .ui

        # подключаем обработчики к кнопкам по их objectName из .ui
        self.btnSchema.clicked.connect(self.create_schema)
        self.btnAdd.clicked.connect(self.add_expense)
        self.btnShow.clicked.connect(self.show_report)

    def create_schema(self):
        try:
            schema = Path(__file__).resolve().parent.parent / "schema.sql"
            sql = schema.read_text(encoding="utf-8-sig")
            with db.tx() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
            QMessageBox.information(self, "Готово", "Схема создана/обновлена.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка схемы", str(e))

    def add_expense(self):
        AddExpenseDialog(self).exec()  # модально

    def show_report(self):
        ReportDialog(self).exec()      # модально (можешь .show() если нужно немодально)

def main():
    setup_logging()
    app = QApplication(sys.argv)

    # подхват QSS
    qss_path = Path(__file__).resolve().parent / "style.qss"
    if qss_path.exists():
        app.setStyleSheet(qss_path.read_text(encoding="utf-8"))

    win = Main()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
