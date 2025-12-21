def generate_summary(slo_result, anomaly_label: str) -> str:
    return (
        f"p95 latency was {slo_result['p95_latency']} ms. "
        f"There were {slo_result['breaches']} SLO breaches. "
        f"Overall system status is classified as {anomaly_label}."
    )
