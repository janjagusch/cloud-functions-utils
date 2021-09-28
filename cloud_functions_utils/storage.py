"""
This module provides a function to upload an object string to Google Cloud Storage.
"""

import os
import warnings
from typing import Optional

from google.cloud import storage


def to_bucket_v2(
    *,
    bucket_name: str,
    blob_name: str,
    obj_data: Optional[str] = None,
    obj_filename: Optional[str] = None
):
    """
    Uploads an object to a path in a Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the bucket.
        blob_name (str): The path inside the bucket where the object should be stored.
        obj_data (str): The content of the object you want to store.
            Mutually exclusive with `obj_filename`.
        obj_filename (str): The path to the file you want to store.
            Mutually exclusive with `obj_data`

    Raises:
        ValueError: If not one of `obj_data` and `obj_filename` is defined.
    """
    if not (obj_data or obj_filename) or (obj_data and obj_filename):
        raise ValueError("Either obj_data or obj_filename must be provided.")
    storage_client = storage.Client()
    storage_bucket = storage_client.bucket(bucket_name)
    storage_blob = storage_bucket.blob(blob_name)
    if obj_data:
        storage_blob.upload_from_string(obj_data)
    else:
        storage_blob.upload_from_filename(obj_filename)


def to_bucket(obj_str, filepath, bucket=None):
    """
    Uploads an object string to a filepath in a Google Cloud Storage bucket.
    Deprecated, please use `to_bucket_v2` instead.

    Args:
        obj_str (str): The object string.
        filepath (str): The filepath.
        bucket (str, optional): The bucket. If not provided, defaults to
            `os.environ["GCF_UTILS_STORAGE_BUCKET"]`.
    """
    warnings.warn(
        "This function is deprecated and will be removed in a future release. "
        "Please use `to_bucket_v2` instead."
    )
    bucket = bucket or os.environ["GCF_UTILS_STORAGE_BUCKET"]
    to_bucket_v2(
        bucket_name=bucket,
        blob_name=filepath,
        obj_data=obj_str,
    )
