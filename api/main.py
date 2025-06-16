from fastapi import FastAPI
import numpy as np
from .model_loader import load_model
from .schemas import LoanInput
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Loan Prediction API", version="1.0.0")

# Mount frontend at root URL
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load ML model
model = load_model()

# API endpoints under /api prefix
app.get("/api/", response_model=dict)
async def root():
    return {"message": "Loan Predictor API is running"}

app.get("/api/health", response_model=dict)
async def health():
    return {"status": "ok"}

app.post("/api/predict")
async def predict(data: LoanInput):
    try:
        input_array = np.array([list(data.dict().values())])
        prediction = model.predict(input_array)[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        return {"error": str(e), "prediction": 0}