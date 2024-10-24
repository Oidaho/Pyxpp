# pyxpp/cli/validate.py
"""_summary_"""
import os
from typing import Union

def DirectoryPath(path: Union[str, bytes]) -> bool:
    """
    Validate if the specified path is a directory.

    Args:
        path (Union[str, bytes]): The path to validate.

    Returns:
        bool: True if the path is a directory, False otherwise.
    """
    return os.path.isdir(path)
