from fastapi import FastAPI,Query
from .schemas import CalcPiResponse, CheckProgressResponse
from .tasks import calculate_pi_task
from celery.result import AsyncResult
from .celery_app import celery_app
app = FastAPI(title="Async π Calculator", version="0.0.1")

@app.get("/calculate_pi", response_model=CalcPiResponse)
def calculate_pi(n: int = Query(..., ge=1, le=10_000)):
   task = calculate_pi_task.delay(n)
   return {"task_id": task.id}

@app.get("/check_progress", response_model=CheckProgressResponse)
def check_progress(task_id: str = Query(...)):
    result = AsyncResult(task_id, app=celery_app)

    if result.successful():
        return {"state": "FINISHED", "progress": 1.0, "result": result.get()}

    if result.state == "PROGRESS" and isinstance(result.info, dict):
        progress = float(result.info.get("progress", 0.0))
        return {"state": "PROGRESS", "progress": progress, "result": None}

    return {"state": "PROGRESS", "progress": 0.0, "result": None}
