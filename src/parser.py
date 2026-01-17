"""Parsing helpers."""

from .models import Record


def parse_line(line: str) -> Record:
    parts = [p.strip() for p in line.split(',', 1)]
    key = parts[0] if parts else ''
    value = parts[1] if len(parts) > 1 else ''
    return Record(key=key, value=value)


def parse_lines(lines):
    return [parse_line(line) for line in lines if line.strip()]
