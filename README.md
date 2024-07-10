# Модуль processing

## Описание:

Функция filter_by_state возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
Функция sort_by_date возвращает новый список, отсортированный по дате

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/MTG-Studio/pyproject.git
```

2. Установите зависимости:
```
black 24.4.2
flake8 7.1.0
isort 5.13.2
mypy 1.10.1
```

## Использование функции filter_by_state:

Функция filter_by_state принимает список словарей и опционально значение для ключа state (по умолчанию 
'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.

Пример входных данных:

```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
Выход функции со статусом по умолчанию 'EXECUTED':
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
Выход функции, если вторым аргументов передано 'CANCELED':
```
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```

## Использование функции sort_by_date:

Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание), и возвращает новый список, отсортированный по дате.

Пример входных данных:
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
Выход функции (сортировка по убыванию):
```
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
