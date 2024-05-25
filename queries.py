from typing import Union

from sqlalchemy import case, func, select
from sqlalchemy.orm import Session

from database import Application, Department

__all__ = (
    'get_departments',
    'get_department_by_id',
    'get_departments_statistics',
)


def get_department_by_id(
        session: Session,
        department_id: int,
) -> Union[Department, None]:
    return session.get(Department, {'id': department_id})


def get_departments(session: Session) -> list[Department]:
    return list(session.scalars(select(Department).order_by('id')))


def get_departments_statistics(session: Session):
    statement = (
        select(
            Department.id,
            Department.name,
            func.max(Application.department_score),
            func.min(Application.department_score),
            func.avg(Application.department_score),
            func.max(Application.ort_score),
            func.min(Application.ort_score),
            func.avg(Application.ort_score),
            func.max(Application.english_score),
            func.min(Application.english_score),
            func.avg(Application.english_score),
            func.count(Application.number),
        )
        .join(Department)
        .where(Application.has_passed)
        .group_by(Department.id)
        .order_by(Department.id)
    )
    return session.execute(statement).all()
