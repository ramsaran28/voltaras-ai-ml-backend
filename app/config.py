import os

# GCP settings
PROJECT_ID = os.getenv("GCP_PROJECT", "your-gcp-project-id")
DATASET_ID = "voltaras"
TABLE_ID = "metrics"

# Cloud Storage
REPORTS_BUCKET = "voltaras-reports"

# SLO config
SLO_LATENCY_MS = 300
