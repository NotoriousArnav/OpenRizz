from fastapi import FastAPI
from langserve import add_routes
from chain import chain
from typing import Dict

app = FastAPI(
    title="OpenRizz",
    description="OpenRizz is a simple API to give you Pickup lines and Flirt lines",
)

@app.get("/", response_model=Dict)
async def root():
    return {"message": "Hello World"}

add_routes(app, chain, path="/rizz")
