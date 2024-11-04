from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserInDB(UserBase):
    hashed_password: str


class UserResponse(UserBase):
    class Config:
        orm_mode = True


class UserSignin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
