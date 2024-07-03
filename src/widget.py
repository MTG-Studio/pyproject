import os


def mask_account_card(account_card: str) -> str:
    """Маскирует и отображает номер карты в формате 'Visa Platinum 7000 79** **** 6361'
    или номер счета в формате 'Счет **4305'"""
    number = ""
    account_card_type = ""
    count = 0
    # Определяется номер карты
    for i in account_card:
        if i.isdigit():
            count += 1
            if count % 4 == 0:
                number = number + i + " "
            else:
                number += i
    # Определяется тип (карта или счет)
    for i in account_card:
        if i.isdigit():
            break
        else:
            account_card_type += i
    if account_card[:4] == "Счет":
        return account_card[:4] + " **" + account_card[-4:]
    else:
        return account_card_type + number[:7] + "** **** " + number[-5:]


def get_date(date: str) -> str:
    """принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024")"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
