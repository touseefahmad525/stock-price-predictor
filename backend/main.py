from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.stock import router as stock_router
from backend.routes.chart import router as chart_router

app = FastAPI(title="Stock Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://your-netlify-site.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stock_router)
app.include_router(chart_router)


@app.get("/")
def home():
    return {"message": "API is running"}
