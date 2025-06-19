from pydantic import BaseModel


class Predict(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float
    contract: str
    internet_service: str
    online_security: str
    tech_support: str
    # churn: bool
