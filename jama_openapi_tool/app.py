import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from py_jama_rest_client.client import JamaClient

load_dotenv()

client = JamaClient(
    os.getenv("JAMA_BASE_URL"),
    credentials=(
        os.getenv("JAMA_CLIENT_ID"),
        os.getenv("JAMA_CLIENT_SECRET"),
    ),
    oauth=True,
)

app = FastAPI(
    title="Jama Toolset",
    version="0.1.0",
    description="Minimal proxy for Jama Connect — only current user info",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

class User(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str


def _fetch_current_user() -> User:
    """Retrieve the current Jama user."""
    try:
        u = client.get_current_user()
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

    return User(
        id=u["id"],
        username=u["username"],
        firstName=u["firstName"],
        lastName=u["lastName"],
        email=u["email"],
    )


@app.get("/users/current", response_model=User, summary="Get current authenticated user")
def get_current_user():
    return _fetch_current_user()


@app.get("/me", response_model=User, summary="Get current authenticated user")
def get_me():
    return _fetch_current_user()
