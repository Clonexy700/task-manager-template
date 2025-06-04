from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import date, datetime

class ShiftTaskBase(BaseModel):
    is_closed: Optional[bool] = Field(..., description="Статус закрытия")
    task_description: Optional[str] = Field(..., description="Описание задания на смену")
    work_center: Optional[str] = Field(..., description="Рабочий центр")
    shift: Optional[str] = Field(..., description="Смена")
    team_name: Optional[str] = Field(..., description="Бригада")
    batch_id: Optional[int] = Field(..., description="Номер партии")
    batch_date: Optional[date] = Field(..., description="Дата партии")
    nomenclature: Optional[str] = Field(..., description="Номенклатура")
    ekn_code: Optional[int] = Field(..., description="Код ЕКН")
    rc_id: Optional[int] = Field(..., description="Идентификатор РЦ")
    shift_start: Optional[datetime] = Field(..., description="Дата начала смены")
    shift_end: Optional[datetime] = Field(..., description="Дата окончания смены")


class ShiftTaskCreate(ShiftTaskBase):
    pass

class ShiftTaskRead(ShiftTaskBase):
    id: int

    class Config:
        orm_mode = True

class ShiftTaskUpdate(ShiftTaskBase):
    is_closed: Optional[bool] = None
    task_description: Optional[str] = None
    work_center: Optional[str] = None
    shift: Optional[str] = None
    team_name: Optional[str] = None
    batch_id: Optional[int] = None
    batch_date: Optional[date] = None
    nomenclature: Optional[str] = None
    ekn_code: Optional[int] = None
    rc_id: Optional[int] = None
    shift_start: Optional[datetime] = None
    shift_end: Optional[datetime] = None

