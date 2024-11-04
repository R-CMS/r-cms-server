from app.core.db.database import get_db
from app.models.chemical import Chemical
from app.models.relation.chemicalProduct import ChemicalProduct


def get_all():
    with next(get_db()) as db:
        return db.query(Chemical).all()


def get_with_products():
    with next(get_db()) as db:
        return db.query(ChemicalProduct).all()
