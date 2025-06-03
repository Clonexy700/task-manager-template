from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import date, datetime

class ShiftTaskBase(BaseModel):
    is_closed: bool = Field(..., description="Статус закрытия")
    task_description: str = Field(..., description="Описание задания на смену")
    work_center: str = Field(..., description="Рабочий центр")
    shift: str = Field(..., description="Смена")