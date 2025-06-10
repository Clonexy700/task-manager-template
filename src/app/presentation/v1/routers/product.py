from typing import List
from datetime import time, datetime, date

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from src.app.presentation.v1.schemas.product import ProductRead, ProductCreate
from src.app.infrastructure.db.session import get_bd
from src.app.infrastructure.db.repositories.product_repo_sqlalchemy import ProductRepositorySQLAlchemy
from src.app.infrastructure.db.repositories.shift_task_repo_sqlalchemy import ShiftTaskRepositorySQLAlchemy
from src.app.application.services.product_service import ProductsService
from src.app.domain.exceptions import DomainError
from src.app.utils.transform import domain_to_read, domains_to_read_list

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/",
             response_model=List[ProductRead],
             status_code=status.HTTP_201_CREATED
             )
def create_products(
        items: List[ProductCreate],
        db: Session = Depends(get_bd)
):
    shift_task_repo = ShiftTaskRepositorySQLAlchemy(db)
    product_repo = ProductRepositorySQLAlchemy(db)
    service = ProductsService(product_repo, shift_task_repo)

    payloads = [item.model_dump() for item in items]
    try:
        created = service.create_products(payloads)
    except DomainError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    return created