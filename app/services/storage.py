from app.crud.storage import get_all


def retrieve_storages():
    storages = get_all()

    return storages
