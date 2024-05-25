from pydantic import BaseModel, ConfigDict, field_validator

__all__ = ('Department',)


class Department(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class ScoresStatistics(BaseModel):
    score_max: float
    score_min: float
    score_avg: float

    @field_validator('score_avg', mode='after')
    @classmethod
    def round_score_average(cls, value: float) -> float:
        return round(value, 2)


class DepartmentStatistics(BaseModel):
    department: Department
    department_score: ScoresStatistics
    ort_score: ScoresStatistics
    english_score: ScoresStatistics
    passed_applications_count: int
