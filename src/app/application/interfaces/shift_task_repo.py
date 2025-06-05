from abc import ABC, abstractmethod
from typing import List, Optional

from src.app.domain.models.shift_task import ShiftTask

class IShiftTaskRepository(ABC):
    @abstractmethod
    def add_many(self, tasks: List[ShiftTask]) -> List[ShiftTask]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self, skip: int = 0, limit: int = 100) -> List[ShiftTask]:
        raise NotImplementedError

    @abstractmethod
    def get(self, task_id: int) -> Optional[ShiftTask]:
        raise NotImplementedError

    def update(self, task_id: int, updates: dict) -> ShiftTask:
        raise NotImplementedError