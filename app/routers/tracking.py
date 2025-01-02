from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas
from app.dependencies import get_db

router = APIRouter(prefix="/tracking", tags=["tracking"])

@router.get("/{good_id}", response_model=schemas.Good)
def track_good(good_id: int, db: Session = Depends(get_db)):
    # Retrieve good details from database
    # ...
    return