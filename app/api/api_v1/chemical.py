from fastapi import APIRouter, status

from app.schemas.response import CommonResponse
from app.services.chemical import retrieve_all, retrieve_with_products

router = APIRouter()


@router.get("/", response_model=CommonResponse, status_code=status.HTTP_200_OK)
def read_chemicals():
    return CommonResponse(
        status=200,
        data=retrieve_all()
    )


@router.get("/products", response_model=CommonResponse, status_code=status.HTTP_200_OK)
def read_with_products():
    return CommonResponse(
        status=200,
        data=retrieve_with_products()
    )
