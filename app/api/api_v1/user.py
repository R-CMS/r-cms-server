from fastapi import APIRouter, Depends, status

from app.schemas.response import CommonResponse
from app.schemas.user import UserCreate, UserResponse, UserSignin
from app.services.user import register_user, signin_user, get_current_user

router = APIRouter()


@router.post("/signup", response_model=CommonResponse, status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate):
    register_user(user)
    return CommonResponse(
        status=201,
        message="sign up completed(username: {})".format(user.username),
        data=user.username
    )


@router.post("/signin", response_model=CommonResponse, status_code=status.HTTP_200_OK)
def signin(user: UserSignin):
    access_token = signin_user(user)
    return CommonResponse(
        status=200,
        data=access_token
    )


@router.get("/me", response_model=CommonResponse, status_code=status.HTTP_200_OK)
def read_information(current_user: UserResponse = Depends(get_current_user)):
    return CommonResponse(
        status=200,
        data=current_user
    )
