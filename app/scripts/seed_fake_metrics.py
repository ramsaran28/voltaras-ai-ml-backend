import random
import datetime
from google.cloud import bigquery

# Initialize BigQuery client
client = bigquery.Client()

rows = []

# Timezone-aware UTC datetime
start = datetime.datetime.now(datetime.UTC)

for i in range(60):
    rows.append({
        "experiment_id": "demo-1",
        "timestamp": (start + datetime.timedelta(seconds=i * 10)).isoformat(),
        "cpu_usage": round(random.uniform(20, 70), 2),
        "latency_ms": random.choice([200, 250, 280, 450]),
        "error_rate": round(random.uniform(0, 0.05), 4),
    })

table_id = "voltaras.metrics"

# Load job config (batch load, free-tier safe)
job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_APPEND"
)

# Run load job
load_job = client.load_table_from_json(
    rows,
    table_id,
    job_config=job_config
)

# Wait for completion
load_job.result()

print("Fake metrics loaded successfully using batch load")
