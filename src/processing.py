import datetime


def filter_by_state(dictionary_list: list, state='EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""
    result_list = []
    for i in dictionary_list:
        if i['state'] == state:
            result_list.append(i)
    return result_list


def sort_by_date(dictionary_list: list, is_reversed_sort=True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(dictionary_list, key=lambda dictionary:
                         dictionary['date'], reverse=is_reversed_sort)
    return sorted_list


dict_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

# Проверка работы функции filter_by_state:
print(filter_by_state(dict_list, "EXECUTED"))
print(filter_by_state(dict_list, "CANCELED"))

# Проверка работы функции sort_by_date:
print(sort_by_date(dict_list, True))
print(sort_by_date(dict_list, False))
print(sort_by_date([
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2020-10-14T08:21:33.419441'}])
)
print(sort_by_date(
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '19-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
         ]))
