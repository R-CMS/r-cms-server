from fastapi import APIRouter, status

from app.schemas.response import CommonResponse
from app.services.storage import retrieve_storages

router = APIRouter()


@router.get("/", response_model=CommonResponse, status_code=status.HTTP_200_OK)
def read_storages():
    return CommonResponse(
        status=200,
        data=retrieve_storages()
    )
