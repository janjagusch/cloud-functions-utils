"""
This module provides a function to upload an object string to Google Cloud Storage.
"""

import os

from google.cloud import storage


def to_bucket(obj_str, filepath, bucket=None):
    """
    Uploads an object string to a filepath in a Google Cloud Storage bucket.

    Args:
        obj_str (str): The object string.
        filepath (str): The filepath.
        bucket (str, optional): The bucket. If not provided, defaults to
            `os.environ["GCF_UTILS_STORAGE_BUCKET"]`.
    """
    bucket = bucket or os.environ["GCF_UTILS_STORAGE_BUCKET"]

    storage_client = storage.Client()
    storage_bucket = storage_client.bucket(bucket)
    storage_blob = storage_bucket.blob(filepath)

    storage_blob.upload_from_string(obj_str)
