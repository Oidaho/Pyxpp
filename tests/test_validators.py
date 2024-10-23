# tests/test_validators.py
"""
A file containing test classes of validation functions
for input data to the CLi interface
"""

from pathlib import Path
import pytest

from pyxpp.cli.validate import FilePath, DirectoryPath
from pyxpp.cli.exceptions import (
    WrongExtensionError,
    NonExistentFileError,
    NonExistentDirectoryError,
)


#! FilePath func
class TestFilePathValidator:
    """File path validator tests for 'input' positional argument"""

    @pytest.mark.parametrize(
        "input_path, file_name",
        [
            ("tests\\test_files\\code.py", "code.py"),
        ],
    )
    def test_correct_file_path(self, input_path, file_name):
        result = FilePath(input_path)
        assert isinstance(result, Path)
        assert result.name == file_name

    @pytest.mark.parametrize(
        "input_path, expected_exception",
        [
            ("awfawf", NonExistentFileError),
            ("tests\\test_files\\some_file.md", NonExistentFileError),
            ("tests\\test_files", NonExistentFileError),
            ("tests\\test_files\\some_file.txt", WrongExtensionError),
        ],
    )
    def test_file_path_exceptions(self, input_path, expected_exception):
        with pytest.raises(expected_exception):
            FilePath(input_path)


#! DirectoryPath func
class TestDirectoryPathValidator:
    """Directory validator tests for '-o' flag"""

    @pytest.mark.parametrize(
        "output_path, directory_name",
        [
            ("tests\\test_files", "test_files"),
        ],
    )
    def test_correct_directory_path(self, output_path, directory_name):
        result = DirectoryPath(output_path)
        assert isinstance(result, Path)
        assert result.name == directory_name

    @pytest.mark.parametrize(
        "output_path, expected_exception",
        [
            ("awfawfwf", NonExistentDirectoryError),
            ("tests\\test_images", NonExistentDirectoryError),
            ("tests\\test_files\\some_file.txt", NonExistentDirectoryError),
        ],
    )
    def test_directory_path_exceptions(self, output_path, expected_exception):
        with pytest.raises(expected_exception):
            DirectoryPath(output_path)
