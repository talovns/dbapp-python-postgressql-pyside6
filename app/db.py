import time
import json
import logging
from contextlib import contextmanager
from pathlib import Path

import psycopg2
import psycopg2.extras

log = logging.getLogger(__name__)

def load_config():
    cfg_file = Path(__file__).resolve().parent / "config_example.json"
    cfg = json.loads(cfg_file.read_text(encoding="utf-8-sig"))
    # зачистим пробелы
    for k, v in list(cfg.items()):
        if isinstance(v, str):
            cfg[k] = v.strip()
    return cfg

CFG = load_config()

def get_conn():
    log.debug("DB connect %s@%s:%s/%s", CFG["user"], CFG.get("host","127.0.0.1"), CFG.get("port",5432), CFG["dbname"])
    return psycopg2.connect(
        dbname=CFG["dbname"],
        user=CFG["user"],
        password=CFG["password"],
        host=CFG.get("host","127.0.0.1"),
        port=CFG.get("port",5432),
    )

@contextmanager
def tx():
    with get_conn() as conn:
        try:
            yield conn
            conn.commit()
            log.debug("tx committed")
        except Exception:
            conn.rollback()
            log.exception("tx rolled back due to error")
            raise

def _run(cur, sql, params=None):
    t0 = time.perf_counter()
    try:
        cur.execute(sql, params or [])
    finally:
        dt = (time.perf_counter() - t0) * 1000
        p = repr(params)[:800] if params is not None else ""
        log.debug("SQL (%.1f ms): %s | params=%s", dt, " ".join(sql.split()), p)

def execute(sql, params=None):
    with tx() as conn:
        with conn.cursor() as cur:
            _run(cur, sql, params)

def fetchall(sql, params=None):
    with tx() as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            _run(cur, sql, params)
            rows = cur.fetchall()
            log.debug("rows fetched: %d", len(rows))
            return rows
