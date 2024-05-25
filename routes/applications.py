from collections.abc import Iterable
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import queries
from database import get_session

router = APIRouter(prefix='/applications', tags=['Applications'])


def parse_departments_statistics(
        departments_statistics: Iterable[tuple],
) -> list[models.DepartmentStatistics]:
    for department_statistics in departments_statistics:
        (
            department_id,
            department_name,
            department_score_max,
            department_score_min,
            department_score_average,

        ) = department_statistics



@router.get('/departments-statistics')
def get_departments_statistics(
        session: Annotated[Session, Depends(get_session, use_cache=False)],
) -> list[models.DepartmentStatistics]:
    print( queries.get_departments_statistics(session))
    return []
