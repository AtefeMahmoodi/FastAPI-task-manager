from fastapi import FastAPI
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

# Include routers
from .routers import tasks
app.include_router(tasks.router)