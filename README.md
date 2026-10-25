# Multi-Container 2-Tier App with Docker Compose

A simple 2-tier application featuring a Python/Flask web app and a PostgreSQL database orchestrated using Docker Compose.

## Features
- **Custom Bridge Network:** Secure inter-container communication.
- **Data Persistence:** PostgreSQL data backed up with Docker Named Volume.
- **Environment Variables:** Dynamic database configurations.

## how to run 
docker compose up --build -d
docker compose ps
## verify in a brower
http://localhost:5000
## Expected Output:
JSON
{"message": "Connected successfully!", "visit_count": 1}

## Verify Data Persistence:
docker compose down
## Bring them back up:
docker compose up -d
