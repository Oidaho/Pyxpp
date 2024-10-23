# pyxpp/cli/exceptions.py
"""_summary_"""

from argparse import ArgumentTypeError


class WrongExtensionError(ArgumentTypeError):
    """A child class that flexibly implements an error in which
    the input file extension does not match the required format.
    """

    pass


class NonExistentPathError(ArgumentTypeError):
    """A child class that flexibly implements an error in which
    the specified directory or file does not exist.
    """

    pass
