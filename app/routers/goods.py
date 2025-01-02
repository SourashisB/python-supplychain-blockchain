from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db, get_web3
from web3 import Web3

router = APIRouter(prefix="/goods", tags=["goods"])

@router.post("/", response_model=schemas.Good)
def create_good(good: schemas.GoodCreate, db: Session = Depends(get_db), w3: Web3 = Depends(get_web3)):
    # Deploy smart contract and create good
    # ...
    return

@router.put("/{good_id}")
def transfer_good(good_id: int, to: str, db: Session = Depends(get_db), w3: Web3 = Depends(get_web3)):
    return