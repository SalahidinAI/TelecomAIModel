from telecom_app.db.database import SessionLocal
from telecom_app.db.model import Customer
from telecom_app.db.schema import Predict
from fastapi import APIRouter, Depends, HTTPException
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

customer_router = APIRouter(prefix='/customer', tags=['Customer'])

BASE_DIR = Path(__file__).resolve().parent.parent.parent

model_path = BASE_DIR / 'model_log.pkl'
scaler = BASE_DIR / 'scaler.pkl'

model = joblib.load(model_path)
scaler = joblib.load(scaler)


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@customer_router.post('/predict/')
async def predict(customer: Predict):
    customer_dict = customer.dict()

    contract = customer_dict.pop('contract')
    internet_service = customer_dict.pop('internet_service')
    online_security = customer_dict.pop('online_security')
    tech_support = customer_dict.pop('tech_support')

    contract_0_1 = [
        1 if contract == 'One year' else 0,
        1 if contract == 'Two year' else 0,
    ]
    internet_service_0_1 = [
        1 if internet_service == 'Fiber optic' else 0,
        1 if internet_service == 'No' else 0,
    ]
    online_security_0_1 = [
        1 if online_security == 'No internet service' else 0,
        1 if online_security == 'Yes' else 0,
    ]
    tech_support_0_1 = [
        1 if tech_support == 'No internet service' else 0,
        1 if tech_support == 'Yes' else 0,
    ]

    features = (list(customer_dict.values()) + contract_0_1 +
                internet_service_0_1 + online_security_0_1 + tech_support_0_1)

    scaled = scaler.transform([features])
    prediction = model.predict(scaled)[0]
    probability = model.predict_proba(scaled)[0][1]
    return {'prediction': f'{bool(prediction)}', 'probability': f'{probability * 100:.1f}'}
    
