from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.compose import router as compose_router

app = FastAPI(title="My FastAPI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(compose_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI project!"}