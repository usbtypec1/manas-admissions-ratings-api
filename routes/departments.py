from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from pydantic import TypeAdapter
from sqlalchemy.orm import Session

import models
import queries
from database import get_session

router = APIRouter(prefix='/departments', tags=['Departments'])


@router.get('')
def get_departments(
        session: Annotated[Session, Depends(get_session, use_cache=False)],
) -> list[models.Department]:
    departments = queries.get_departments(session)
    type_adapter = TypeAdapter(list[models.Department])
    return type_adapter.validate_python(departments)


@router.get('/{department_id}')
def get_department(
        session: Annotated[Session, Depends(get_session, use_cache=False)],
        department_id: int,
) -> models.Department:
    department = queries.get_department_by_id(session, department_id)
    if department is None:
        raise HTTPException(status_code=404, detail='Department not found')
    return models.Department.model_validate(department)
