import os


def get_mask_card_number(card: str) -> str:
    """Маскирует и отображает номер карты в формате XXXX XX** **** XXXX"""
    mask = card[:6] + "*" * (len(card) - 10) + card[(len(card) - 4):]
    result_mask = ""
    for i in range(len(mask)):
        if (i + 1) % 4 == 0:
            result_mask += mask[i] + " "
        else:
            result_mask += mask[i]
    return result_mask


def get_mask_account(account: str) -> str:
    """Маскирует и отображает номер счета в формате **XXXX"""
    return "**" + account[(len(account) - 4):]
