from typing import List, Optional

from sqlalchemy.orm import Session
from sqlalchemy import  Column, Integer, String, Boolean, Date, DateTime

from src.app.application.interfaces.shift_task_repo import IShiftTaskRepository
from src.app.domain.models.shift_task import ShiftTask as DomainShiftTask, ShiftTask
from src.app.infrastructure.db.base import Base

class ShiftTaskORM(Base):
    __tablename__ = "shift_tasks"

    id = Column(Integer, primary_key=True, index=True)
    is_closed = Column(Boolean, index=True, default=False, nullable=False)
    task_description = Column(String, nullable=False)
    work_center = Column(String, nullable=False)
    shift = Column(String, nullable=False)
    team_name = Column(String, nullable=False)
    batch_id = Column(Integer, nullable=False)
    batch_date = Column(Date, nullable=False)
    nomenclature = Column(String, nullable=False)
    ekn_code = Column(Integer, nullable=False)
    rc_id = Column(Integer, nullable=False)
    shift_start = Column(DateTime, nullable=False)
    shift_end = Column(DateTime, nullable=False)


class ShiftTaskRepositorySQLAlchemy(IShiftTaskRepository):
    def __init__(self, db_session: Session):
        self._db = db_session

    def add_many(self, tasks: List[DomainShiftTask]) -> List[DomainShiftTask]:
        orm_objects = []
        for task in tasks:
            orm = ShiftTaskORM(
                is_closed=task.is_closed,
                task_description=task.task_description,
                work_center=task.work_center,
                shift=task.shift,
                team_name=task.team_name,
                batch_id=task.batch_id,
                batch_date=task.batch_date,
                nomenclature=task.nomenclature,
                ekn_code=task.ekn_code,
                rc_id=task.rc_id,
                shift_start=task.shift_start,
                shift_end=task.shift_end,
            )
            self._db.add(orm)
            orm_objects.append(orm)


        self._db.commit()
        for orm in orm_objects:
            self._db.refresh(orm)

        result: List[DomainShiftTask] = []
        for orm in orm_objects:
            dom = DomainShiftTask(
                id=orm.id,
                is_closed=orm.is_closed,
                task_description=orm.task_description,
                work_center=orm.work_center,
                shift=orm.shift,
                team_name=orm.team_name,
                batch_id=orm.batch_id,
                batch_date=orm.batch_date,
                nomenclature=orm.nomenclature,
                ekn_code=orm.ekn_code,
                rc_id=orm.rc_id,
                shift_start=orm.shift_start,
                shift_end=orm.shift_end,
            )
            result.append(dom)
        return result

    def list_all(self, skip: int = 0, limit: int = 100) -> List[DomainShiftTask]:
        rows = self._db.query(ShiftTaskORM).offset(skip).limit(limit).all()
        return [
            DomainShiftTask(
                id=row.id,
                is_closed=row.is_closed,
                task_description=row.task_description,
                work_center=row.work_center,
                shift=row.shift,
                team_name=row.team_name,
                batch_id=row.batch_id,
                batch_date=row.batch_date,
                nomenclature=row.nomenclature,
                ekn_code=row.ekn_code,
                rc_id=row.rc_id,
                shift_start=row.shift_start,
                shift_end=row.shift_end,
            )
            for row in rows
        ]

    def get(self, task_id: int) -> Optional[DomainShiftTask]:
        row = self._db.query(ShiftTaskORM).filter(ShiftTaskORM.id == task_id).first()
        if not row:
            return None
        return DomainShiftTask(
            id=row.id,
            is_closed=row.is_closed,
            task_description=row.task_description,
            work_center=row.work_center,
            shift=row.shift,
            team_name=row.team_name,
            batch_id=row.batch_id,
            batch_date=row.batch_date,
            nomenclature=row.nomenclature,
            ekn_code=row.ekn_code,
            rc_id=row.rc_id,
            shift_start=row.shift_start,
            shift_end=row.shift_end,
        )
