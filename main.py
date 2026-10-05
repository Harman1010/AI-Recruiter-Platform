from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from backend.routes.jobs import job_route

from backend.routes.candidates import candidate_route

from backend.routes.matches import route as match_route

from backend.routes.ranking import ranking_route

app = FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500","https://ai-recruiter-platform-frontend.vercel.app"],
    allow_headers = ["*"],
    allow_methods = ["*"],
    allow_credentials=True
)

app.include_router(job_route)

app.include_router(candidate_route)

app.include_router(match_route)

app.include_router(ranking_route)