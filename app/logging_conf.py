import logging
import sys
import json
from logging.handlers import RotatingFileHandler
from pathlib import Path

class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": self.formatTime(record, datefmt="%Y-%m-%dT%H:%M:%S"),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        extra = getattr(record, "extra", None)
        if isinstance(extra, dict):
            payload.update(extra)
        return json.dumps(payload, ensure_ascii=False)

def setup_logging():
    base = Path(__file__).resolve().parent.parent
    app_log = base / "app.log"
    audit_log = base / "audit.log"

    # ---- техлог (SQL, ошибки и т.п.) ----
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    file_h = RotatingFileHandler(app_log, maxBytes=1_000_000, backupCount=3, encoding="utf-8")
    file_h.setLevel(logging.DEBUG)
    file_h.setFormatter(fmt)
    root.addHandler(file_h)

    console_h = logging.StreamHandler(sys.stdout)
    console_h.setLevel(logging.INFO)
    console_h.setFormatter(fmt)
    root.addHandler(console_h)

    # ---- отдельный аудит действий (JSONL) ----
    audit = logging.getLogger("audit")
    audit.setLevel(logging.INFO)
    audit.propagate = False

    audit_h = RotatingFileHandler(audit_log, maxBytes=1_000_000, backupCount=5, encoding="utf-8")
    audit_h.setLevel(logging.INFO)
    audit_h.setFormatter(JsonFormatter())
    audit.addHandler(audit_h)

    # необработанные исключения -> app.log
    def excepthook(exctype, value, tb):
        logging.getLogger("sys.excepthook").exception("Uncaught exception", exc_info=(exctype, value, tb))
    sys.excepthook = excepthook
