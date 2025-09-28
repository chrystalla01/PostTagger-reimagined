from .celery_app import celery_app

@celery_app.task(bind=True)
def calculate_pi_task(self, n: int) -> str:
    self.update_state(state="PROGRESS", meta={"progress": 0.0})
    raise NotImplementedError("Monte Carlo π calculation not implemented yet")
