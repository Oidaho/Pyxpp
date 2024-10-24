import pytest
import os
from pyxpp.cli.validate import DirectoryPath

class TestDirectoryPathValidator:

    def test_valid_directory(self):
        # Create a temporary directory for testing
        os.makedirs('test_dir', exist_ok=True)
        assert DirectoryPath('test_dir') is True
        os.rmdir('test_dir')  # Clean up

    def test_invalid_directory(self):
        assert DirectoryPath('non_existent_dir') is False

    def test_file_path(self):
        # Create a temporary file for testing
        with open('test_file.txt', 'w') as f:
            f.write('test')
        assert DirectoryPath('test_file.txt') is False
        os.remove('test_file.txt')  # Clean up

    def test_empty_string(self):
        assert DirectoryPath('') is False
