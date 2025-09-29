from .celery_app import celery_app
from decimal import Decimal, getcontext
import random
SAMPLES_PER_BATCH = 100000

@celery_app.task(bind=True)
def calculate_pi_task(self, n: int) -> str:
    """
        Monte Carlo pi (batched for progress).

        Idea: throw random points in [0,1]×[0,1]; count those with x^2 + y^2 ≤ 1.
        Ratio in_circle / total ≈ pi/4  ⇒  pi ≈ 4 * (in_circle / total).

        Progress: split work into `batches = max(20, n // 2)`. After each batch of
        SAMPLES_PER_BATCH points, call update_state(progress = i / batches).

        Precision: set Decimal precision to n+5 as a small safety margin, then
        format the final estimate to exactly n decimal places.

        Tiny example: if after 100,000 points, 78,600 are inside, pi ≈ 4*(78600/100000)=3.144,
        then we return it formatted to n decimals.
     """
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
