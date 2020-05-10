"""
This module provides a function to insert rows into a Google BigQuery table.
"""

from datetime import datetime
import os

from google.cloud import bigquery

from .exceptions import EmptyRowsError, InsertionError


def _add_inserted_at_field(rows):
    inserted_at = datetime.now()
    for row in rows:
        row.update({"inserted_at": inserted_at})


def to_table(rows, project=None, dataset=None, table=None, add_inserted_at=True):
    """
    Inserts rows into Google BigQuery.

    Args:
        rows (list[dict]): The rows.
        project (str, optional): The name of the Google Cloud project. If not provided,
            defaults to `os.environ["GCF_UTILS_PROJECT"]`.
        dataset (str, optional): The name of the Google BigQuery dataset. If not
            provided, defaults to `os.environ["GCF_UTILS_BIGQUERY_DATASET"]`.
        table (str, optional): The name of the Google BigQuery table. If not provided,
            defaults to `os.environ["GCF_UTILS_BIGQUERY_TABLE"]`.
        add_inserted_at (bool, optional): If true, adds an `inserted_at` field with
            the current datetime to all rows.

    Raises:
        EmptyRowsError: When they rows object is an empty list.
        InsertionError: When an error occurs while inserting rows to BigQuery.
    """

    if not rows:
        raise EmptyRowsError

    project = project or os.environ["GCF_UTILS_PROJECT"]
    dataset = dataset or os.environ["GCF_UTILS_BIGQUERY_DATASET"]
    table = table or os.environ["GCF_UTILS_BIGQUERY_TABLE"]

    bq_client = bigquery.Client()
    bq_dataset = bigquery.dataset.DatasetReference.from_string(f"{project}.{dataset}")
    bq_table = bq_dataset.table(table)

    if add_inserted_at:
        _add_inserted_at_field(rows)

    errors = bq_client.insert_rows(bq_client.get_table(bq_table), rows)
    if errors:
        raise InsertionError(errors)
