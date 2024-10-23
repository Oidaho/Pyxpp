# pyxpp/cli/exceptions.py
"""_summary_"""

from argparse import ArgumentTypeError


class WrongExtensionError(ArgumentTypeError):
    """A child class that flexibly implements an error in which
    the input file extension does not match the required format.
    """

    pass


class NonExistentFileError(ArgumentTypeError):
    """A child class that flexibly implements an error in which
    the target file does not exist or its directory.
    """

    pass


class NonExistentDirectoryError(ArgumentTypeError):
    """A child class that flexibly implements an error in which
    the target directory does not exist or its file.
    """

    pass
