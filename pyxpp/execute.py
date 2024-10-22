# pyxpp/execute.py
"""_summary_"""

from .cli import cli_parser


def main() -> None:
    """An entry point directly invoked via poetry.scripts"""
    cli_parser.parse_args()
