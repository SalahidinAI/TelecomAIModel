from fastapi import FastAPI
import uvicorn
from telecom_app.api import telecom


telecom_app = FastAPI(title='Telecom')
telecom_app.include_router(telecom.customer_router)


if __name__ == '__main__':
    uvicorn.run(telecom_app, host='127.0.0.1', port=8000)
