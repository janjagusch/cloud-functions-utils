"""
Helper functions for Google Cloud Services.
"""

from itertools import islice
import re

from .bigquery import to_table
from .error_reporting import error_reporting
from .pub_sub import to_topic, decode
from .storage import to_bucket


def chunks(iterable, chunksize=500):
    """
    Breaks down an iterable into chunks.
    """
    iterable = iter(iterable)
    while True:
        chunk = tuple(islice(iterable, chunksize))
        if not chunk:
            return
        yield chunk


def camel_to_snake(term):
    """
    Converts a CamedCased term into a snake_cased term.
    """
    pattern = re.compile(r"(?<!^)(?=[A-Z])")
    return pattern.sub("_", term).lower()
