"""
Custom exceptions for this package.
"""


class CloudFunctionsUtilsError(Exception):
    """
    Abstract parent exception for this package.
    """


class InsertionError(CloudFunctionsUtilsError):
    """
    Error that is thrown when insertion into Google BigQuery does not succeed.
    """


class EmptyRowsError(CloudFunctionsUtilsError):
    """
    Error that is thrown when trying to insert an empty list to Google BigQuery.
    """
