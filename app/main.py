from fastapi import FastAPI
from app.routers import goods, tracking

app = FastAPI()

app.include_router(goods.router)
app.include_router(tracking.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Blockchain-based Supply Chain Tracking"}