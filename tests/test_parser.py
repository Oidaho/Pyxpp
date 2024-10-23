# tests/test_validators.py
"""_summary_"""

from pathlib import Path

import pytest

from pyxpp.parser import CodeParser

# For these tests, it is guaranteed that this path has passed validation
TETS_FILE_1 = "tests\\test_files\\code.py"
TETS_FILE_2 = "tests\\test_files\\code2.py"  # Intentional Syntax Error


class TestCodeParser:
    """_summary_"""

    def test_init(self):
        input_file = Path(TETS_FILE_1)
        parser = CodeParser(input_file)

        assert isinstance(parser, CodeParser)

        # TODO: This test depends on the future architecture of the class
        # ! Finish the test later

    @pytest.mark.parametrize(
        "input_path, expected_sequence",
        [
            (
                TETS_FILE_1,
                ["p", "r", "i", "n", "t", "(", '"', "f", '"', ")", "\n", "EOF"],
            ),
            (
                TETS_FILE_2,
                ["i", "f", " ", "1", ":", "\n", " ", " ", " ", " ", "g", "\n", "EOF"],
            ),
        ],
    )
    def test_parsing_summary(self, input_path, expected_sequence):
        input_file = Path(input_path)
        parser = CodeParser(input_file)

        summary = list(parser.consistently())

        assert summary == expected_sequence
