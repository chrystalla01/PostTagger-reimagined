from typing import Literal, Optional
from pydantic import BaseModel, Field

TaskState = Literal["PROGRESS", "FINISHED"]

class CalcPiResponse(BaseModel):
    task_id: str

class CheckProgressResponse(BaseModel):
    state: TaskState = Field(..., description="PROGRESS or FINISHED")
    progress: float = Field(..., ge=0.0, le=1.0)
    result: Optional[str] = None
