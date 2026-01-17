"""Validation logic."""

from .models import Record


def is_valid(record: Record) -> bool:
    return bool(record.key) and bool(record.value)


def validate_all(records):
    return [r for r in records if is_valid(r)]
