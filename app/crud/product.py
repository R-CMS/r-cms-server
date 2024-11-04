from app.core.db.database import get_db
from app.models.product import Product


def get_all():
    with next(get_db()) as db:
        return db.query(Product).all()
