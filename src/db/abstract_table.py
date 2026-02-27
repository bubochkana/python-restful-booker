"""Abstract database table query layer.

This module provides a generic abstraction for SQLAlchemy ORM models.
It defines a reusable base class that encapsulates common query
operations and returns results wrapped in a GenericResults helper.
"""

from __future__ import annotations

from typing import Any, Dict, Generic, Type, TypeVar

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

    def get_all(self) -> GenericResults[Dict[str, Any]]:
        """Retrieve all records for the configured model.

        Returns:
            GenericResults[Dict[str, Any]]: Wrapper containing mapping
            representations of all rows in the table.
        """
        stmt = select(self.cls)
        result = self.session.execute(stmt).mappings().all()
        return GenericResults(result)
