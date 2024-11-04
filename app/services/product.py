from app.crud.product import get_all


def retrieve_products():
    product = get_all()
    return product
