import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def dict_list():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


# Параметризация тестов для различных возможных значений статуса
@pytest.mark.parametrize("state, expected", [
    ('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
    ('ANY', []),
    (111, [])
])
def test_filter_by_date(dict_list, state, expected):
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(dict_list, state) == expected


def test_filter_by_date_wrong_type(dict_list):
    assert filter_by_state(dict_list, state=1) == []


def test_filter_by_date_invalid_dict():
    """Проверка работы функции при отсутствии словарей с указанным статусом state в списке"""
    with pytest.raises(KeyError):
        filter_by_state([{'id': 41428829, 'stat': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'stat': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                         {'id': 594226727, 'stat': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                         {'id': 615064591, 'stat': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],
                        state='CANCELED')


@pytest.mark.parametrize("is_reversed_sort, expected", [
    (False, [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),
    (True, [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
    ('ANY', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
])
def test_sort_by_date(dict_list, is_reversed_sort, expected):
    """Тестирование сортировки списка словарей по датам в порядке убывания и возрастания"""
    assert sort_by_date(dict_list, is_reversed_sort) == expected


def test_sort_by_date_same_date(dict_list):
    """Проверка корректности сортировки при одинаковых датах"""
    assert sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2020-10-14T08:21:33.419441'}]
    ) == [{'id': 615064591, 'state': 'CANCELED', 'date': '2020-10-14T08:21:33.419441'},
          {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}]
