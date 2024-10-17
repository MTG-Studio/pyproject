transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


def filter_by_currency(transact, currency):
    count = 0
    while True:
        if count >= len(transact):
            yield None
        else:
            if transact[count]["operationAmount"]["currency"]["code"] == currency:
                yield transact[count]
        count += 1


def transaction_descriptions(transact):
    descriptions_list = []
    count = 0
    while True:
        if count >= len(transact):
            yield None
        else:
            descriptions_list.append(transact[count].get("description"))
            yield descriptions_list[count]
        count += 1


def card_number_generator(start, stop):
    if start < 0:
        start = 0
    if stop > 9999999999999999:
        stop = 9999999999999999
    while start <= stop:
        format_card = "{:016d}".format(start)
        yield format_card[:4] + " " + format_card[4:8] + " " + format_card[8:12] + " " + format_card[12:]
        start += 1


# Проверка работы функции filter_by_currency
usd_transactions = filter_by_currency(transactions, "RUB")
for i in range(3):
    print(next(usd_transactions))


# Проверка работы функции transaction_descriptions
descriptions = transaction_descriptions(transactions)
for i in range(6):
    print(next(descriptions))


# Проверка работы функции card_number_generator
for card_number in card_number_generator(-1, 50):
    print(card_number)
