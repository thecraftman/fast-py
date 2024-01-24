# fastapi_app.py
from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

# Instrument FastAPI
FastAPIInstrumentor.instrument_app(app)

@app.get("/")
async def read_root():
    return {"message": "Welcome to my FastAPI application!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Additional routes and logic for your FastAPI app
