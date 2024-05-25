from datetime import datetime

from sqlalchemy import ForeignKey, URL, create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    relationship,
    sessionmaker,
)

import config

__all__ = (
    'engine',
    'get_session',
    'Application',
    'Department',
)

url = URL.create(
    drivername='postgresql+psycopg2',
    username=config.POSTGRES_USER,
    host=config.POSTGRES_HOST,
    port=5432,
    database=config.POSTGRES_DATABASE,
    password=config.POSTGRES_PASSWORD,
)

engine = create_engine(url)
session_factory = sessionmaker(engine)


def get_session() -> Session:
    with session_factory() as session:
        yield session


class Base(DeclarativeBase):
    pass


class Department(Base):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    applications = relationship('Application', back_populates='department')

    def __repr__(self) -> str:
        return f'<Department(id={self.id!r}, name={self.name!r})>'


class Application(Base):
    __tablename__ = 'applications'

    number: Mapped[str] = mapped_column(primary_key=True)
    stage: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int]
    department_score: Mapped[float]
    ort_score: Mapped[float | None]
    english_score: Mapped[float | None]
    created_at: Mapped[datetime]
    department_id: Mapped[int] = mapped_column(ForeignKey('departments.id'))
    has_passed: Mapped[bool]

    department: Mapped[Department] = relationship(
        'Department',
        back_populates='applications',
    )

    def __repr__(self) -> str:
        return f'<Application(number={self.number!r}, rating={self.rating!r}, department_score={self.department_score!r}, ort_score={self.ort_score!r}, english_score={self.english_score!r}, created_at={self.created_at!r}, department_id={self.department_id!r}, has_passed={self.has_passed!r}, stage={self.stage!r})>'
