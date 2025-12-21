import numpy as np


def detect_latency_anomaly(latencies):
    median = np.median(latencies)
    threshold = median * 1.5

    anomalies = latencies > threshold
    score = anomalies.sum() / len(latencies)

    if score > 0.3:
        label = "Incident"
    elif score > 0.1:
        label = "Warning"
    else:
        label = "Normal"

    return float(score), label
