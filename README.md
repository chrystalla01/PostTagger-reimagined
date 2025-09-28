# PostTagger reimagined

Small **FastAPI + Celery** app that computes
n digits of π asynchronously using Redis as a broker
and Monte Carlo for the algorithm.

Currently the project contains:
- FastAPI api with  `/calculate_pi` and `/check_progress` endpoints.
- Celery worker and Redis broker running in Docker Compose.


 ## Run the application
```bash
docker compose up --build
```
- Enter http://localhost:8000/ to see the application running.
- Enter http://127.0.0.1:8000/docs to read the API Docs
