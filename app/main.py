from fastapi import FastAPI,Query,HTTPException
from schemas import CalcPiResponse, CheckProgressResponse
app = FastAPI(title="Async π Calculator", version="0.0.1")

@app.get("/calculate_pi", response_model=CalcPiResponse)
def calculate_pi(n: int = Query(..., ge=1, le=10_000)):
    raise HTTPException(status_code=501, detail="Not implemented yet")

@app.get("/check_progress", response_model=CheckProgressResponse)
def check_progress(task: str = Query(...)):
    raise HTTPException(status_code=501, detail="Not implemented yet")
