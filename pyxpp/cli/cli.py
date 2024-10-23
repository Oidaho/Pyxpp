# pyxpp/cli/cli.py
"""_summary_"""

import argparse

from .validate import FilePath, DirectoryPath


cli = argparse.ArgumentParser(
    prog="pyxpp",
    description="Translator from a variety of Python language to a variety of C++ language.",
    usage="%(prog)s ./code.py [options]",
    epilog=(
        "This software was created solely for educational purposes.\n"
        "Some functions may not work as intended.\n"
        "Regular support for the module is not guaranteed.\n"
    ),
)


cli.add_argument(
    "input",
    help="*.py input file",
    metavar="./code.py",
    type=FilePath,
)


cli.add_argument(
    "-o",
    help="output file path",
    metavar="./cpp_files/",
    required=False,
    type=DirectoryPath,
    default=".",
)
