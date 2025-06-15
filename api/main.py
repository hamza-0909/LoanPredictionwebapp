

from fastapi import FastAPI
import numpy as np
from api.model_loader import load_model
from api.schemas import LoanInput


# ✅ CORS middleware (specific to Live Server at 127.0.0.1:5500)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Add this block before defining any endpoints
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Important: allow OPTIONS, POST, etc.
    allow_headers=["*"],
)


model = load_model()

@app.get("/")
def root():
    return {"message": "Loan Predictor API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: LoanInput):
    input_array = np.array([list(data.dict().values())])
    prediction = model.predict(input_array)[0]
    return {"loan_approved": bool(prediction)}
