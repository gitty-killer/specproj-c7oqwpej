"""Summary builder."""

from .models import Summary
from .validator import is_valid


def build_summary(records):
    total = len(records)
    valid = sum(1 for r in records if is_valid(r))
    invalid = total - valid
    return Summary(total=total, valid=valid, invalid=invalid)
