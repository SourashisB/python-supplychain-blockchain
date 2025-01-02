from web3 import Web3
from app.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_web3():
    w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))
    return w3