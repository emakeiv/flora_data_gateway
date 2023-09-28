from typing import Generator

from app.db.session import LocalSession


def get_db() -> Generator:
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
