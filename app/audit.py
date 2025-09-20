import logging
import uuid
import getpass
import platform

_session_id = str(uuid.uuid4())
_user = getpass.getuser()

_audit = logging.getLogger("audit")

def set_app_user(username: str | None):
    global _user
    if username:
        _user = username

def log_action(action: str, **data):
    """Пишем событие в audit.log (JSON)."""
    _audit.info(action, extra={"extra": {
        "action": action,
        "session": _session_id,
        "user": _user,
        "platform": platform.platform(),
        **data
    }})
