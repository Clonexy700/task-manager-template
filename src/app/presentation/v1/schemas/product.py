from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    unique_code: str = Field(..., description="Уникальный код продукта")
    batch_id: int = Field(..., description="Дата партии")
    batch_date: date = Field(..., description="Дата партии")

class ProductRead(BaseModel):
    id: int
    unique_code: str
    batch_id: int
    is_aggregated: bool
    aggregated_at: Optional[datetime]

    class Config:
        orm_mode = True
