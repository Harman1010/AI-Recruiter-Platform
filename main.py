from fastapi import FastAPI

from backend.routes.jobs import job_route

from backend.routes.candidates import candidate_route

from backend.routes.matches import route as match_route

app = FastAPI()

app.include_router(job_route)

app.include_router(candidate_route)

app.include_router(match_route)