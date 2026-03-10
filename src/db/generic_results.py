"""Generic query results wrapper.

This module defines a reusable container for database query results.
It provides helper utilities, such as conversion of stored results
into a pandas DataFrame.
"""

from __future__ import annotations

from typing import Generic, Iterable, List, Sequence, TypeVar

import pandas as pd

T = TypeVar('T')


class GenericResults(Generic[T]):
    """Wrapper for query results with helper transformation methods.

    Stores query results and provides convenience utilities,
    such as conversion to a pandas DataFrame.
    """

    def __init__(self, result: Sequence[T] | Iterable[T]):
        """Initialize the result wrapper.

        Args:
            result (Sequence[T] | Iterable[T]): Query result collection.
        """
        self._result: List[T] = list(result)

    def as_data_frame(self) -> pd.DataFrame:
        """Convert stored results into a pandas DataFrame.

        Returns:
            pd.DataFrame: DataFrame representation of the stored results.
        """
        return pd.DataFrame(self._result)
