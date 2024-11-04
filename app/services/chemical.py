from app.crud.chemical import get_all, get_with_products


def retrieve_all():
    chemicals = get_all()

    return chemicals


def retrieve_with_products():
    chemicals = get_with_products()

    return chemicals
