
def get_mask_card_number(card: str) -> str:
    """Маскирует и отображает номер карты в формате XXXX XX** **** XXXX"""
    mask = card[:6] + "*" * (len(card) - 10) + card[(len(card) - 4):]
    result_mask = ""
    if len(card) >= 16 and card.isdigit():
        for i in range(len(mask)):
            if (i + 1) % 4 == 0 and (i + 1) < len(mask):
                result_mask += mask[i] + " "
            else:
                result_mask += mask[i]
        return result_mask
    else:
        return "Неверный формат карты"


def get_mask_account(account: str) -> str:
    """Маскирует и отображает номер счета в формате **XXXX"""
    if len(account) >= 6 and account.isdigit():
        return "**" + account[(len(account) - 4):]
    else:
        return "Неверный формат счета"


# Проверка работы функции get_mask_card_number:
print(get_mask_card_number('1033333310344333'))
print(get_mask_card_number(''))

# Проверка работы функции get_mask_account:
print(get_mask_account('2322222455'))
