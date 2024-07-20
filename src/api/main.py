from fastapi import FastAPI
from src.api.prediction_routes import router as prediction_router

app = FastAPI()

app.include_router(prediction_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
