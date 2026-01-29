# Todo Backend API

This is the backend API for the Evolution of Todo - Phase II project, built with FastAPI and SQLModel.

## Features

- RESTful API endpoints for Todo management
- PostgreSQL database with SQLModel ORM
- Complete CRUD operations for todos
- Health check endpoint
- Authentication and authorization

## Database Configuration

### Using Neon DB (Recommended for Production)

1. Create a Neon account at [neon.tech](https://neon.tech)
2. Create a new project in Neon
3. Copy the connection string from your Neon dashboard
4. Create a `.env` file in the backend directory with your credentials:

```bash
cp sample.env .env
# Then edit .env with your Neon DB credentials
```

### Using SQLite (Default for Development)

The application defaults to SQLite if no `DATABASE_URL` is provided. This is suitable for development and testing.

## Endpoints

### Health Check
- `GET /api/health` - Check API health status

### Todo Management
- `GET /api/todos` - Get all todos (with optional filtering and pagination)
- `GET /api/todos/{id}` - Get a specific todo
- `POST /api/todos` - Create a new todo
- `PUT /api/todos/{id}` - Update all fields of a todo
- `PATCH /api/todos/{id}` - Partially update a todo
- `DELETE /api/todos/{id}` - Delete a todo

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
# Copy the sample environment file
cp sample.env .env

# Edit .env with your actual database credentials
# For Neon DB, use the connection string from your Neon dashboard
```

3. Run the application:
```bash
# Option 1: Using the start script (recommended)
python start_server.py

# Option 2: Direct uvicorn command
python -m uvicorn app.main:app --reload
```

### Notes (Windows)

- **DATABASE_URL format**: Put a plain SQLAlchemy URL, for example:
  - `DATABASE_URL=sqlite:///./dev.db`
  - `DATABASE_URL=postgresql://USER:PASSWORD@HOST/DBNAME?sslmode=require`
- **Hot reload**: On some Windows setups, auto-reload can fail. `start_server.py` defaults to `RELOAD=0`.
  - To enable reload: set `RELOAD=1` in `.env`

The API will be available at `http://localhost:8000` or `http://127.0.0.1:8000`.

## CORS Configuration

The application is configured to allow cross-origin requests. By default, it allows all origins (`"*"`), which enables communication with the frontend running on a different port. For production, it's recommended to specify the exact frontend URL.