# PostTagger reimagined

Small **FastAPI + Celery** app that computes
n digits of π asynchronously using Redis as a broker
and Monte Carlo for the algorithm.

Currently the project contains:
- FastAPI api with two endpoints:
  - `GET /calculate_pi?n=<int>` → `{"task_id": "<uuid>"}`
  - `GET /check_progress?task_id=<uuid>` → `{"state": "PROGRESS|FINISHED", "progress": 0..1, "result": null|string}`
- Celery worker and Redis broker running in Docker Compose.

## API Docs
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


 ## Run the application
```bash
docker compose up --build
```

