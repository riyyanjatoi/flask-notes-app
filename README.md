# Flask Notes API

A lightweight Flask REST API containerized using Docker. This project demonstrates Python application development, Git version control, Docker image creation, and container deployment.

## Features

- `GET /` – Returns a welcome message.
- `GET /notes` – Returns a list of notes stored in memory.
- `GET /health` – Returns application health status.

## Tech Stack

- Python 3.12
- Flask
- Docker
- Git & GitHub

## Project Structure

```text
flask-notes-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Prerequisites

- Docker Desktop installed and running.
- Git installed.

## Build Docker Image

Clone the repository:

```bash
git clone https://github.com/riyyanjatoi/flask-notes-app.git
cd flask-notes-app
```

Build the Docker image:

```bash
docker build -t devdeploy .
```

## Run Docker Container

```bash
docker run -d -p 8000:8000 --name flask-notes devdeploy
```

The application will be available at:

`http://localhost:8000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/notes` | Retrieve all notes |
| GET | `/health` | Health status |

## Container Management

View running containers:

```bash
docker ps
```

View application logs:

```bash
docker logs flask-notes
```

Follow logs:

```bash
docker logs -f flask-notes
```

Stop the container:

```bash
docker stop flask-notes
```

Restart the container:

```bash
docker start flask-notes
```

Remove the container:

```bash
docker rm -f flask-notes
```

## Notes

- Notes are stored in application memory and are not persistent.
- The Flask application listens on `0.0.0.0:8000`.
- Docker maps host port `8000` to container port `8000`.
- The Docker image uses the lightweight `python:3.12-slim` base image.

## Author

Muhammad Riyyan

GitHub: [@riyyanjatoi](https://github.com/riyyanjatoi)