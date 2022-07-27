import pytest

# это фикстура для тестов
@pytest.fixture()
def two_numbers_sum():  # запомните это имя
    return 1, 1, 2
