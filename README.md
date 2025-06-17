```markdown
# jama-openapi-tool

**Minimal FastAPI proxy for Jama Connect**  
Expose a `/me` endpoint to fetch the current user’s info via OAuth2 Client Credentials. The legacy `/users/current` route still works but is hidden from the public docs.
Designed for incremental expansion—add more Jama routes as you go.

---

## Features

- 🔒 OAuth2 Client Credentials (Client ID + Client Secret)  
- 📦 `.env` support via `python-dotenv`  
- ⚡ `/me` endpoint for the authenticated user (legacy `/users/current` hidden)
- 🌐 CORS enabled for GET
- 🖥 Simple CLI for launching the server

---

## Prerequisites

- Python 3.8+  
- A Jama Connect account with a **Client ID + Client Secret** (My Profile → Set API Credentials)  
- Network access to your Jama instance  

---

## Installation

Install directly from GitHub:
```bash
pip install git+https://github.com/Wenlin-AI/jama-openapi-tool.git
```

Or clone and install locally:


1. Clone the repo
   ```bash
   git clone https://github.com/Wenlin-AI/jama-openapi-tool.git
   cd jama-openapi-tool
   ```

2. Create & activate a virtual environment  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   ```

3. Install dependencies  
   ```bash
   pip install -e .
   ```

---

## Configuration

Create a file named `.env` in the project root with your Jama credentials:

```ini
# .env
JAMA_BASE_URL=https://yourdomain.jamacloud.com
JAMA_CLIENT_ID=your_client_id
JAMA_CLIENT_SECRET=your_client_secret
```

> **Note:** `.env` is ignored by Git. Never commit secrets to version control.

---

## Running

Start the FastAPI app using the bundled CLI:

```bash
jama-openapi-tool --port 8000
```

- Open `http://localhost:8000/docs` for interactive Swagger UI
- Call `GET /me` to fetch your own user profile (the `/users/current` alias is hidden from docs)

---

## Endpoint

### GET /me (alias: `/users/current`)

Fetch current user’s information from Jama. The `/users/current` path is still available but excluded from the OpenAPI schema.

**Response** (200):

```json
{
  "id": 12345,
  "username": "user.name",
  "firstName": "Henri",
  "lastName": "Dupont",
  "email": "henri@example.com"
}
```

---

## app.py (reference)

```python
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from py_jama_rest_client.client import JamaClient

# Load .env
load_dotenv()

# OAuth2 Client Credentials
client = JamaClient(
    os.getenv("JAMA_BASE_URL"),
    credentials=(
        os.getenv("JAMA_CLIENT_ID"),
        os.getenv("JAMA_CLIENT_SECRET"),
    ),
    oauth=True
)

app = FastAPI(
    title="Jama Toolset",
    version="0.1.0",
    description="Minimal proxy for Jama Connect — only current user info"
)

# Enable CORS for GET
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

@app.get(
    "/users/current",
    response_model=User,
    summary="Get current authenticated user",
    include_in_schema=False,
)
@app.get("/me", response_model=User, summary="Get current authenticated user")
def get_current_user():
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
```

---

## Next Steps

- Add more routes: `/projects`, `/items`, `/filters`, etc.  
- Harden CORS & auth for production  
- Add logging, retries, better error handling  
- Dockerize & deploy  

Feel free to fork and expand!

## Project Documentation
Additional guides and notes live in the [`docs/`](docs/) directory.
