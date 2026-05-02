from fastapi import APIRouter, HTTPException
from backend.services.chart_service import get_stock_chart

router = APIRouter()


@router.get("/chart/{stock_name}")
def stock_chart(stock_name: str):
    try:
        data = get_stock_chart(stock_name)
        return {
            "stock": stock_name,
            "data": data
        }
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Chart data failed to load. Please try another stock symbol.",
        ) from exc
