from app.core.security import get_password_hash, verify_password
from app.core.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate


def get_user_by_username(username: str):
    with next(get_db()) as db:
        return db.query(User).filter(User.username == username).first()


def create_user(user: UserCreate):
    with next(get_db()) as db:
        hashed_password = get_password_hash(user.password)
        db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user


def authenticate_user(username: str, password: str):
    user = get_user_by_username(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False

    return user
