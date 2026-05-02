from fastapi import APIRouter, HTTPException
from backend.services.predictor import run_prediction

router = APIRouter()


@router.get("/predict/{stock_name}")
def predict_stock(stock_name: str):
    try:
        return run_prediction(stock_name)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Please try another stock symbol.",
        ) from exc
