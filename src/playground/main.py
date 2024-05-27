from fastapi import FastAPI
from playground.routers import task

app = FastAPI()

app.include_router(task.router)
