# src/api/main.py
from fastapi import FastAPI
from src.api.prediction_routes import router as prediction_router
import os

app = FastAPI()

app.include_router(prediction_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
