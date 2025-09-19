import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logging():
    log_path = Path(__file__).resolve().parent.parent / "app.log"
    handler = RotatingFileHandler(log_path, maxBytes=512_000, backupCount=2, encoding="utf-8")
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
    handler.setFormatter(fmt)

    root = logging.getLogger()
    root.setLevel(logging.INFO)
    root.addHandler(handler)
