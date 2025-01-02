from pydantic import BaseModel
from datetime import datetime

class GoodBase(BaseModel):
    name: str

class GoodCreate(GoodBase):
    pass

class Good(GoodBase):
    id: int
    manufacturer: str
    distributor: str
    retailer: str
    consumer: str
    timestamp: datetime

    class Config:
        orm_mode = True