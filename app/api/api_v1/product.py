from fastapi import APIRouter, status

from app.schemas.response import CommonResponse
from app.services.product import retrieve_products

router = APIRouter()


@router.get("/", response_model=CommonResponse, status_code=status.HTTP_200_OK)
def read_products():
    return CommonResponse(
        status=200,
        data=retrieve_products()
    )
