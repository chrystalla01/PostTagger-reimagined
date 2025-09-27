from fastapi import FastAPI
app = FastAPI(title="Async π Calculator", version="0.0.1")

@app.get("/health")
def health():
    return {"ok": True}
