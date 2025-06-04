from typing import List

from src.app.application.interfaces.shift_task_repo import IShiftTaskRepository
from src.app.domain.exceptions import DomainError
from src.app.domain.models.shift_task import ShiftTask

class ShiftTaskService:
    def __init__(self, repo: IShiftTaskRepository):
        self._repo = repo

    def create_shift_tasks(self, payloads: List[dict]) -> List[ShiftTask]:
        domain_objects : List[ShiftTask] = []
        for data in payloads:
            try:
                object = ShiftTask(
                    id=None,
                    is_closed=data['is_closed'],
                    task_description=data['task_description'],
                    work_center=data['work_center'],
                    shift=data['shift'],
                    team_name=data['team_name'],
                    batch_id=data['batch_id'],
                    batch_date=data['batch_date'],
                    nomenclature=data['nomenclature'],
                    ekn_code=data['ekn_code'],
                    rc_id=data['rc_id'],
                    shift_start=data['shift_start'],
                    shift_end=data['shift_end']
                )
            except DomainError as exception:
                raise DomainError(f"Неверные данные ShiftTask: {exception}")
            domain_objects.append(object)

        saved = self._repo.add_many(domain_objects)
        return saved

    def list_all(self, skip: int = 0, limit: int = 100) -> List[ShiftTask]:
        return self._repo.list_all(skip=skip, limit=limit)