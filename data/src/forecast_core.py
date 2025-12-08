import pandas as pd
from dataclasses import dataclass

@dataclass
class ForecastParams:
    horizon_weeks: int = 8
    safety_factor: float = 1.2  # 20% safety
    min_stock_threshold: int = 50

def load_site_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df

def forecast_supply(df: pd.DataFrame, params: ForecastParams) -> pd.DataFrame:
    """
    Very simple forecast for demo:
    - Assume patients_on_treatment remains roughly constant.
    - Expected dose per week = patients_on_treatment * (1 - dropout_rate)
    - Apply safety factor.
    - Compare to stock_on_hand to estimate weeks until shortage.
    """
    df = df.copy()

    df["expected_weekly_dose"] = df["patients_on_treatment"] * (1 - df["dropout_rate"])
    df["expected_weekly_dose_safety"] = df["expected_weekly_dose"] * params.safety_factor

    results = []
    grouped = df.groupby("site_id")

    for site_id, group in grouped:
        latest = group.sort_values("week").iloc[-1]
        weekly_need = latest["expected_weekly_dose_safety"]
        stock = latest["stock_on_hand"]

        if weekly_need <= 0:
            weeks_until_shortage = params.horizon_weeks
        else:
            weeks_until_shortage = stock / weekly_need

        shortage_risk = "HIGH" if weeks_until_shortage < latest["lead_time_weeks"] else "LOW"

        results.append({
            "site_id": site_id,
            "current_stock": stock,
            "weekly_need_safety": round(weekly_need, 1),
            "weeks_until_shortage": round(weeks_until_shortage, 1),
            "lead_time_weeks": latest["lead_time_weeks"],
            "shortage_risk": shortage_risk
        })

    return pd.DataFrame(results)
