from fastapi import FastAPI, HTTPException
from app.reporter.reporter import run_report

app = FastAPI(
    title="Voltaras AI/ML Backend",
    version="0.1.0"
)


@app.get("/")
def health_check():
    return {"status": "ok", "service": "Voltaras Backend"}


@app.post("/run-analysis/{experiment_id}")
def run_analysis(experiment_id: str):
    """
    Runs analysis for a given experiment ID and returns:
    - anomaly score
    - SLO result
    - plot URL
    - AI summary
    """

    try:
        result = run_report(experiment_id)

        # Safety fallback (never return None)
        if result is None:
            raise HTTPException(
                status_code=500,
                detail="Analysis completed but returned no data."
            )

        return result

    except Exception as e:
        # Proper error reporting instead of silent crash
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
