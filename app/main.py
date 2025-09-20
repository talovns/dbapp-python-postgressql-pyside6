import sys
from pathlib import Path
import logging
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from .logging_conf import setup_logging
from .ui.ui_mainwindow import Ui_MainWindow  # если ты грузишь .ui на лету — адаптируй
from . import db
from .dialogs import AddExpenseDialog
from .views import ReportDialog
from .audit import log_action, set_app_user

log = logging.getLogger(__name__)

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Трекер расходов (PySide6 + PostgreSQL)")

        # стиль QSS
        qss_path = Path(__file__).resolve().parent / "style.qss"
        if qss_path.exists():
            self.parentApp.setStyleSheet(qss_path.read_text(encoding="utf-8")) if hasattr(self, "parentApp") else None

        # аудит
        set_app_user("demo")  # если у тебя есть реальный логин — подставь его тут
        log_action("app_start", version="1.0")

        # кнопки
        self.btnSchema.clicked.connect(self._on_create_schema)
        self.btnAdd.clicked.connect(self._on_add_expense)
        self.btnShow.clicked.connect(self._on_show_report)

    # обёртки, чтобы фиксировать клики
    def _on_create_schema(self):
        log_action("click", target="btnSchema")
        self.create_schema()

    def _on_add_expense(self):
        log_action("click", target="btnAdd")
        self.add_expense()

    def _on_show_report(self):
        log_action("click", target="btnShow")
        self.show_report()

    def create_schema(self):
        try:
            schema = Path(__file__).resolve().parent.parent / "schema.sql"
            sql = schema.read_text(encoding="utf-8-sig")
            from . import db
            with db.tx() as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
            QMessageBox.information(self, "Готово", "Схема создана/обновлена.")
            log_action("schema_created", ok=True)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка схемы", str(e))
            log.exception("create_schema failed")
            log_action("schema_created", ok=False, error=str(e))

    def add_expense(self):
        log_action("open_dialog", name="AddExpenseDialog")
        dlg = AddExpenseDialog(self)
        dlg.exec()
        log_action("close_dialog", name="AddExpenseDialog")

    def show_report(self):
        log_action("open_dialog", name="ReportDialog")
        dlg = ReportDialog(self)
        dlg.exec()
        log_action("close_dialog", name="ReportDialog")

def main():
    setup_logging()
    app = QApplication(sys.argv)

    # стиль QSS (если не подхватываешь в __init__)
    qss_path = Path(__file__).resolve().parent / "style.qss"
    if qss_path.exists():
        app.setStyleSheet(qss_path.read_text(encoding="utf-8"))

    win = Main()
    # сохраним ссылку на app, если нужно в Main
    win.parentApp = app
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
