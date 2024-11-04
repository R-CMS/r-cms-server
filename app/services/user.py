from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.security import create_access_token, decode_access_token
from app.crud.user import create_user, get_user_by_username, authenticate_user
from app.schemas.user import UserCreate, UserSignin

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/user/signin")


def register_user(user: UserCreate):
    existing_user = get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already registered"
        )
    return create_user(user)


def signin_user(user: UserSignin):
    db_user = authenticate_user(user.username, user.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    return create_access_token(data={"sub": db_user.username})


def get_current_user(token: str = Depends(oauth2_scheme)):
    username = decode_access_token(token)
    print(username)
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = get_user_by_username(username=username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
