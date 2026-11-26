# Flask Notes API

A lightweight Flask REST API containerized using Docker and orchestrated with Docker Compose, backed by PostgreSQL for persistent data storage.

This project demonstrates Python application development, REST API development, Docker image creation, multi-container orchestration, database integration, container networking, persistent volumes, and health checks.

## Features

- `GET /` – Returns a welcome message.
- `GET /notes` – Retrieves all notes stored in PostgreSQL.
- `POST /notes` – Creates a new note in PostgreSQL.
- `GET /health` – Returns application health status.
- PostgreSQL database integration using Psycopg 3.
- Docker Compose for managing multiple containers.
- Named Docker volumes for persistent database storage.
- Automatic database connection retries.
- PostgreSQL health checks and service dependency management.
- Environment-based configuration using `.env`.

## Tech Stack

- Python 3.12
- Flask
- PostgreSQL 17
- Psycopg 3
- Docker
- Docker Compose
- Git & GitHub

## Project Structure

```text
flask-notes-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── .dockerignore
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Prerequisites

- Docker Desktop installed and running.
- Git installed.

No local Python or PostgreSQL installation is required.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/riyyanjatoi/flask-notes-app.git
cd flask-notes-app
```

### Configure Environment Variables

Create a `.env` file using the example configuration:

```bash
cp .env.example .env
```

Update the database credentials in `.env` if necessary.

**Note:** The actual `.env` file contains local credentials and should never be committed to GitHub.

### Build and Start Services

Build the Flask application image and start both containers:

```bash
docker compose up -d --build
```

This starts:

- Flask application on port `8000`.
- PostgreSQL database on port `5432`.

Docker Compose automatically creates a shared network, allowing the Flask application to communicate with PostgreSQL using the service hostname `db`.

### Verify Running Containers

```bash
docker compose ps
```

The PostgreSQL container should report a healthy status.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/notes` | Retrieve all notes |
| POST | `/notes` | Create a new note |
| GET | `/health` | Application health status |

### Create a Note

```bash
curl -X POST http://localhost:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"content":"Learning Docker Compose"}'
```

### Retrieve All Notes

```bash
curl http://localhost:8000/notes
```

### Check Application Health

```bash
curl http://localhost:8000/health
```

## Docker Compose Management

View running services:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs app
```

View database logs:

```bash
docker compose logs db
```

Follow application logs:

```bash
docker compose logs -f app
```

Rebuild and restart services:

```bash
docker compose up -d --build
```

Stop and remove containers:

```bash
docker compose down
```

**Important:** Running `docker compose down` preserves the named database volume. Avoid `docker compose down -v` if you want to retain database records.

## Database Management

Access the PostgreSQL container:

```bash
docker exec -it notes-db psql -U notesuser -d notesdb
```

Retrieve all notes directly from PostgreSQL:

```sql
SELECT * FROM notes ORDER BY id;
```

Exit PostgreSQL:

```sql
\q
```

## Data Persistence

PostgreSQL data is stored using a named Docker volume:

```yaml
volumes:
  postgres_data:
```

This ensures database records remain available even when containers are stopped, removed, and recreated.

The application and database communicate through Docker Compose's default network, while the database health check ensures PostgreSQL is ready before the Flask application starts.

## Environment Configuration

The application uses environment variables for database configuration.

| Variable | Description |
|---|---|
| `POSTGRES_USER` | PostgreSQL username |
| `POSTGRES_PASSWORD` | PostgreSQL password |
| `POSTGRES_DB` | Database name |
| `POSTGRES_PORT` | Host port for PostgreSQL |
| `DATABASE_URL` | Connection string used by Flask |

Actual credentials are stored in `.env`, while `.env.example` provides placeholder configuration.

## Notes

- The Flask application listens on `0.0.0.0:8000`.
- Docker maps host port `8000` to container port `8000`.
- PostgreSQL runs inside its own container.
- The Flask application connects to PostgreSQL through the Compose service hostname `db`.
- Database records persist through a named Docker volume.
- PostgreSQL readiness is monitored using `pg_isready`.
- Database connection retries help handle startup timing.

## Author

**Muhammad Riyyan**

GitHub: [@riyyanjatoi](https://github.com/riyyanjatoi)