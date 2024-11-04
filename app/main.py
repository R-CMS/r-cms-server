from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1 import user, chemical, product, storage
from app.core.config import settings
from app.core.db import Base, engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware, # type: ignore
    allow_origins=settings.ORIGINS.split(','),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(user.router, prefix="/api/v1/users")
app.include_router(chemical.router, prefix="/api/v1/chemicals")
app.include_router(product.router, prefix="/api/v1/products")
app.include_router(storage.router, prefix="/api/v1/storages")
