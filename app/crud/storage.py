from app.core.db.database import get_db
from app.models.storage import Storage


def get_all():
    with next(get_db()) as db:
        return db.query(Storage).all()
