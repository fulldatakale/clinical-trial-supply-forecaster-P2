from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from pathlib import Path
import pandas as pd
from .forecast_core import ForecastParams, forecast_supply

app = FastAPI(title="Clinical Trial Supply Forecaster")

@app.post("/forecast_csv")
async def forecast_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        return JSONResponse({"error": "Please upload a CSV file."}, status_code=400)

    contents = await file.read()
    df = pd.read_csv(
        filepath_or_buffer=Path(file.filename),
        # For simplicity we read from the bytes using StringIO:
        # but we can use: pd.read_csv(io.BytesIO(contents)) instead
    )
    # Correct approach:
    import io
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    params = ForecastParams()
    result_df = forecast_supply(df, params)
    return result_df.to_dict(orient="records")
