"""
This module provides a decorator class to report errors to Google Cloud.
"""

import functools
import logging
import warnings
from typing import Callable, Optional

from google.cloud.error_reporting import Client


def error_reporting_v2(*, raise_error: Optional[bool] = True) -> Callable:
    """
    Create decorator that adds error reporting to a function.

    Reports errors to Stackdriver and to function logs.

    Args:
        raise_ (Optional[bool]): Whether to raise the error after it has been logged.

    Returns:
        Callable: A decorator.
    """
    def decorator(func: Callable):
        client = Client()
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except BaseException as error:
                client.report_exception()
                logging.error(error)
                if raise_error:
                    raise error
        return wrapper
    return decorator


# pylint: disable=invalid-name
class error_reporting:
    """
    This class serves as a decorator to report errors to Google Cloud.

    Args:
        func (callable): The function you want to decorate.
    """

    def __init__(self, func):
        warnings.warn(
            "This function is deprecated and will be removed in a future release. "
            "Please use `error_reporting_v2` instead."
        )
        self._func = func
        self._client = Client()

    def __call__(self, *args, **kwargs):
        try:
            self._func(*args, **kwargs)
        except Exception as error:
            self._client.report_exception()
            raise error


# pylint: enable=invalid-name
