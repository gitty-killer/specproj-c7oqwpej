"""CLI entry point."""

import sys
from .parser import parse_lines
from .summarize import build_summary


def main():
    records = parse_lines(sys.stdin.readlines())
    summary = build_summary(records)
    print(f"total={summary.total} valid={summary.valid} invalid={summary.invalid}")


if __name__ == '__main__':
    main()
