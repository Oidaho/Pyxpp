# pyxpp/cli/validate.py
"""_summary_"""

import argparse
import os


def file_exists(file_path):
    """Проверка существования файла."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"Файл {file_path} не существует.")
    return file_path
