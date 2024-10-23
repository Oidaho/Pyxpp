# pyxpp/execute.py
"""_summary_"""

from .cli import cli


def main() -> None:
    """An entry point directly invoked via poetry.scripts"""
    cli.parse_args()
