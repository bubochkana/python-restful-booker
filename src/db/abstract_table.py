"""Abstract database table query layer.

This module provides a generic abstraction for SQLAlchemy ORM models.
It defines a reusable base class that encapsulates common query
operations and returns results wrapped in a GenericResults helper.
"""

from __future__ import annotations

from typing import Generic, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.db.generic_results import GenericResults

TModel = TypeVar('TModel')


class AbstractTable(Generic[TModel]):
    """Base query abstraction for database tables.

    Provides common query operations for SQLAlchemy ORM models.
    Child classes supply the model class and active database session.
    """

    def __init__(self, model_cls: Type[TModel], session: Session):
        """Initialize the table abstraction.

        Args:
            model_cls (Type[TModel]): SQLAlchemy ORM model class.
            session (Session): Active SQLAlchemy session.
        """
        self.cls: Type[TModel] = model_cls
        self.session: Session = session

    def get_all(self) -> GenericResults[TModel]:
        """Retrieve all records for the configured model.

        Executes a SELECT statement for the model associated with this
        table abstraction and returns the results wrapped in
        ``GenericResults``.

        Returns:
            GenericResults[TModel]: Wrapper containing all retrieved records.
        """
        stmt = select(self.cls)
        result = self.session.execute(stmt).mappings().all()
        return GenericResults(result)

    def get_by(self, op_query) -> Optional[TModel]:
        """Retrieve a single record matching the given condition.

        Args:
            op_query: SQLAlchemy boolean expression used in the WHERE clause.

        Returns:
            Optional[TModel]: Matching ORM object if found, otherwise ``None``.
        """
        stmt = select(self.cls).where(op_query)
        return self.session.scalar(stmt)
