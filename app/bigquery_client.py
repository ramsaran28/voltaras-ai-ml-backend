import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def fetch_metrics(experiment_id: str) -> pd.DataFrame:
    """
    Temporary local data generator.
    This replaces BigQuery until real data is available.
    """

    # Generate fake timestamps
    now = datetime.utcnow()
    timestamps = [now - timedelta(minutes=i) for i in range(50)][::-1]

    # Generate fake latency data (ms)
    latency = np.random.normal(loc=120, scale=15, size=50)

    df = pd.DataFrame({
        "experiment_id": experiment_id,
        "timestamp": timestamps,
        "latency_ms": latency
    })

    return df
