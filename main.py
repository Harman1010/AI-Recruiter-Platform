print("MAIN: starting import")

from fastapi import FastAPI

print("FAST API imported")

from fastapi.middleware.cors import CORSMiddleware

print("Middlware ready!")


from backend.routes.jobs import job_route

print("JOB route ready!")

from backend.routes.candidates import candidate_route

print("candidate_route imported")

from backend.routes.matches import route as match_route

print("match_route imported!")

from backend.routes.ranking import ranking_route

print("ranking_route imported!")

app = FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_headers = ["*"],
    allow_methods = ["*"],
    allow_credentials=True
)

app.include_router(job_route)

print("job_route included")

app.include_router(candidate_route)

print("candidate_route included")

app.include_router(match_route)

print("match_route included")

app.include_router(ranking_route)

print("ranking_route included!")