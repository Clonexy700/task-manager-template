from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.app.presentation.v1.schemas.shift_task import ShiftTaskCreate, ShiftTaskRead
from src.app.infrastructure.db.session import get_bd
from src.app.infrastructure.db.repositories.shift_task_repo_sqlalchemy import ShiftTaskRepositorySQLAlchemy
from src.app.application.services.shift_task_service import ShiftTaskService
from src.app.domain.exceptions import DomainError

router = APIRouter(prefix="/shift-tasks", tags=["Shift Tasks"])

@router.post(
    "/",
    response_model=List[ShiftTaskRead],
    status_code=status.HTTP_201_CREATED
)
def create_shift_tasks(
        tasks_in: List[ShiftTaskCreate],
        db: Session = Depends(get_bd)
):
    repo = ShiftTaskRepositorySQLAlchemy(db)
    service = ShiftTaskService(repo)

    tasks_data = [task.dict() for task in tasks_in]

    try:
        created_objects = service.create_shift_tasks(tasks_data)
    except DomainError as exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exception))

    result = []
    for dom in created_objects:
        result.append(
            ShiftTaskRead(
                id=dom.id,
                is_closed=dom.is_closed,
                task_description=dom.task_description,
                work_center=dom.work_center,
                shift=dom.shift,
                team_name=dom.team_name,
                batch_id=dom.batch_id,
                batch_date=dom.batch_date,
                nomenclature=dom.nomenclature,
                ekn_code=dom.ekn_code,
                rc_id=dom.rc_id,
                shift_start=dom.shift_start,
                shift_end=dom.shift_end,
            )
        )

    return result

@router.get("/{task_id}",
            response_model=ShiftTaskRead,
            status_code=status.HTTP_200_OK
           )
def get_shift_task_by_id(task_id: int, db: Session = Depends(get_bd)):
    repo = ShiftTaskRepositorySQLAlchemy(db)
    service = ShiftTaskService(repo)

    try:
        dom = service.get_shift_task(task_id)
    except DomainError as exception:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exception))

    return ShiftTaskRead(
        id=dom.id,
        is_closed=dom.is_closed,
        task_description=dom.task_description,
        work_center=dom.work_center,
        shift=dom.shift,
        team_name=dom.team_name,
        batch_id=dom.batch_id,
        batch_date=dom.batch_date,
        nomenclature=dom.nomenclature,
        ekn_code=dom.ekn_code,
        rc_id=dom.rc_id,
        shift_start=dom.shift_start,
        shift_end=dom.shift_end,
    )


