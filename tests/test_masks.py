import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card, expected",
                         [("4272678916515987", "4272 67** **** 5987"),
                          ("4272678916515987010", "4272 67** **** ***7 010"),
                          ("42726fd916515987", "Неверный формат карты"),
                          ("87010", "Неверный формат карты"),
                          ("", "Неверный формат карты")])
def test_masks_card_basic(card, expected):
    assert get_mask_card_number(card) == expected


def test_masks_card_wrong_type():
    with pytest.raises(TypeError):
        get_mask_card_number(1)


@pytest.mark.parametrize("account, expected", [('4272678916515987', '**5987'),
                                               ('4272678916515987010', '**7010'),
                                               ('42726fd916515987010', 'Неверный формат счета'),
                                               ('87010', 'Неверный формат счета'),
                                               ('', 'Неверный формат счета')])
def test_masks_account_basic(account, expected):
    assert get_mask_account(account) == expected


def test_masks_account_wrong_type():
    with pytest.raises(TypeError):
        get_mask_account(1)