from fastapi import FastAPI

from backend.routes.jobs import route

app = FastAPI()

app.include_router(route)