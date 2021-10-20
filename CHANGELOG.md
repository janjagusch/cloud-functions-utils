# Changelog

## 0.5.0

- Added `error_reporting_v2`, which allow to specify whether an error should be raised.
- Deprecated `error_reporting`. Please use `error_reporting_v2` instead.
- Made package compatible with latest version of `google-cloud` packages.

## 0.4.0

- Added `to_bucket_v2` which allows to specify a filepath, instead of providing a string.
- Deprecated `to_bucket`. Please use `to_bucket_v2` instead.

## 0.3.0

- The `to_topic` function does not wait until all messages are published anymore. Instead, it returns the future objects.

## 0.2.4

- Fixed bug in `pub_sub.py`.

## 0.2.3

- Made base64 de/encoding in `pub_sub.py` optional.

## 0.2.2

- Fixed bug in `bigquery.py`.

## 0.2.1

- Fixed bug in `bigquery.py`.

## 0.2.0

- Cleaned up code.

## 0.1.0

- Initial version.
