import random
from datetime import datetime

def run_report(experiment_id: str):
    """
    Demo-safe report generator.
    Works even without BigQuery or Cloud Storage.
    """

    latency_samples = [random.randint(80, 140) for _ in range(20)]
    avg_latency = sum(latency_samples) / len(latency_samples)

    anomaly_score = round(random.uniform(0.05, 0.25), 2)
    status = "NORMAL" if anomaly_score < 0.2 else "ANOMALY"

    slo = round(1 - anomaly_score, 2)

    return {
        "experiment_id": experiment_id,
        "timestamp": datetime.utcnow().isoformat(),
        "avg_latency_ms": round(avg_latency, 2),
        "anomaly_score": anomaly_score,
        "status": status,
        "slo": slo,
        "plot_url": None,
        "ai_summary": (
            "Latency is within expected bounds and SLO is healthy."
            if status == "NORMAL"
            else "Latency spikes detected; investigate downstream services."
        )
    }
