from .celery_app import celery_app
from decimal import Decimal, getcontext
import random
SAMPLES_PER_BATCH = 5000

@celery_app.task(bind=True)
def calculate_pi_task(self, n: int) -> str:

    getcontext().prec = n + 5
    batches = max(20, n // 2)
    points_in_circle = 0
    total_points = 0

    for i in range(1, batches + 1):
        for _ in range(SAMPLES_PER_BATCH):
            x, y = random.random(), random.random()
            if x * x + y * y <= 1:
                points_in_circle += 1
        total_points += SAMPLES_PER_BATCH
        self.update_state(state="PROGRESS", meta={"progress": i / batches})

    pi_est = Decimal(4) * Decimal(points_in_circle) / Decimal(total_points)

    return f"{pi_est:.{n}f}"
