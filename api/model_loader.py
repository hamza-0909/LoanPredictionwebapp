import joblib
import os

def load_model():
    return joblib.load("models/best_model.pkl")


