# pyxpp/cli/validate.py
"""_summary_"""

from pathlib import Path

from .exceptions import WrongExtensionError, NonExistentPathError


def FilePath(input_path: str) -> Path:
    """Checks the existence of the file at the specified path
    and ensures it has the .py extension.

    Args:
        input_path (str): Input path to the file.

    Raises:
        WrongExtensionError: _description_
        NonExistentPathError: _description_

    Returns:
        Path: Pathlib Path Object.
    """
    path_obj = Path(input_path)
    if not path_obj.is_file():
        raise NonExistentPathError(
            f"'{path_obj}' is not a file or does not exist.",
        )

    if path_obj.suffix != ".py":
        raise WrongExtensionError(
            f"'{path_obj}' must have the .py extension.",
        )

    return path_obj


def DirectoryPath(output_path: str) -> Path:
    """Checks the existence of the specified directory.
    Args:
        output_path (str): _description_

    Raises:
        ...

    Returns:
        Path: Pathlib Path Object.
    """
    path_obj = Path(output_path)

    # TODO: Write me

    return path_obj
