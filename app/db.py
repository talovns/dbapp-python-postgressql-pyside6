import json
import logging
import psycopg2
import psycopg2.extras as extras
from contextlib import contextmanager
from pathlib import Path

log = logging.getLogger(__name__)

def load_config():
    cfg_file = Path(__file__).resolve().parent / "config_example.json"
    with open(cfg_file, "r", encoding="utf-8") as f:
        return json.load(f)

CFG = load_config()

def get_conn():
    return psycopg2.connect(
        dbname=CFG["dbname"],
        user=CFG["user"],
        password=CFG["password"],
        host=CFG.get("host","127.0.0.1"),
        port=CFG.get("port",5432),
    )

@contextmanager
def tx():
    conn = get_conn()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        log.exception("DB error -> rollback")
        raise
    finally:
        conn.close()

def execute(sql, params=None):
    with tx() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)

def fetchall(sql, params=None):
    with get_conn() as conn, conn.cursor(cursor_factory=extras.DictCursor) as cur:
        cur.execute(sql, params)
        return cur.fetchall()
