from fastapi import FastAPI
from fastapi_playground.routers import task

app = FastAPI()

app.include_router(task.router)
