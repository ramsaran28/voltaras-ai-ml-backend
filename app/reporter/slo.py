from app.config import SLO_LATENCY_MS


def compute_slo(latencies):
    p95 = latencies.quantile(0.95)
    max_latency = latencies.max()
    breaches = (latencies > SLO_LATENCY_MS).sum()

    score = max(0, 100 - breaches * 2)

    return {
        "p95_latency": float(p95),
        "max_latency": float(max_latency),
        "breaches": int(breaches),
        "score": int(score),
    }
