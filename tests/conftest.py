"""
Файл conftest.py — это файл, который позволяет определять фикстуры, которые могут быть доступны
для всех тестов в проекте, без необходимости импортировать их в каждый тестовый файл.
"""

import pytest


@pytest.fixture
def numbers():
    return "321"


@pytest.fixture
def letters():
    return "olleh"


@pytest.fixture
def number_list():
    return [1, 2, 3, 4, 5]
