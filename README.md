# FastAPI Projects

A collection of projects built while learning FastAPI, progressing from basic routing to a full-stack REST API with authentication and database integration.

## Projects

### class1 — Cats API (Basic)
Simple CRUD API for a cats resource. Covers path/query parameters, Pydantic validation, and HTTP status codes.

### class2 — Cats API (Enhanced)
Extended version with additional validation and refined request/response patterns.

### TodoApp — Full-Stack Todo API
A production-style REST API with user authentication and a relational database.

**Features:**
- JWT authentication (OAuth2 password flow, bcrypt password hashing)
- Role-based access control — users manage their own todos; admins can access all
- Full CRUD for todos scoped to the authenticated user
- User profile and password change endpoints
- Pydantic v2 request validation

**Stack:** FastAPI · SQLAlchemy · PostgreSQL (initially SQLite) · python-jose · passlib

**Routers:** `auth` · `todos` · `admin` · `user`

## Setup

```bash
# Install dependencies
uv sync

# Run any project
uvicorn TodoApp.main:app --reload
```

Interactive API docs available at `http://127.0.0.1:8000/docs`.
