from fastapi import FastAPI
from views import router
from models import Base
from dbSettings import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
