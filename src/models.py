"""Data models."""

from dataclasses import dataclass

@dataclass
class Record:
    key: str
    value: str

@dataclass
class Summary:
    total: int
    valid: int
    invalid: int
