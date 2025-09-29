# PostTagger reimagined

Small **FastAPI + Celery** app that computes
n digits of π asynchronously using Redis as a broker
and Monte Carlo for the algorithm.

Currently the project contains:
- FastAPI api with two endpoints:
  - `GET /calculate_pi?n=<int>` → `{"task_id": "<uuid>"}`
  - `GET /check_progress?task_id=<uuid>` → `{"state": "PROGRESS|FINISHED", "progress": 0..1, "result": null|string}`
- Celery worker and Redis broker running in Docker Compose.


## How it works (Monte Carlo)
We estimate π by sampling random points in the unit square and counting how many fall inside the quarter circle (x² + y² ≤ 1).  
The ratio ≈ π/4, so π ≈ 4 × (points_in_circle / total_points). The task runs in batches to report smooth progress (0..1). We format the final value to exactly *n* decimals.

## API Docs
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

 ## Run the application
```bash
git clone <repo-url>
cd <repo-folder>
#build and start
docker compose up --build 
#verify services
docker copose ps
#should show task registered
docker compose logs -f worker
```
## Start a job
curl "http://localhost:8000/calculate_pi?n=20"
## Poll
curl "http://localhost:8000/check_progress?task_id=<ID>"
## Stop
`docker compose down`
## Common issues 
- API 404 on /: expected (no root route). Use /docs, /calculate_pi, /check_progress.

- “unregistered task”: rebuild after clone: `docker compose up -d --build `

- Can’t reach Docker: start Docker Desktop.
