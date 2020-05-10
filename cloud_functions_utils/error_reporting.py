"""
This module provides a decorator class to report errors to Google Cloud.
"""

from google.cloud.error_reporting import Client


# pylint: disable=invalid-name
class error_reporting:
    """
    This class serves as a decorator to report errors to Google Cloud.

    Args:
        func (callable): The function you want to decorate.
    """

    def __init__(self, func):
        self._func = func
        self._client = Client()

    def __call__(self, *args, **kwargs):
        try:
            self._func(*args, **kwargs)
        except Exception as error:
            self._client.report_exception()
            raise error


# pylint: enable=invalid-name
