from fastapi import FastAPI
from .database import engine
from . import models
from .routers import tasks

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(tasks.router)