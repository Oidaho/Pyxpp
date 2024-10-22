# pyxpp/cli/cli.py
"""_summary_"""

import argparse

from .validate import file_exists


cli_parser = argparse.ArgumentParser(
    prog="pyxpp",
    description="Translator from a variety of Python language to a variety of C++ language.",
    usage="pyxpp [-h] -i code.py",
)

cli_parser.add_argument(
    "-i",
    help="*.py input file path",
    required=True,
    type=file_exists,
    metavar="./code.py",
)
