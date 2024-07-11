import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_masks_basic():
    assert get_mask_card_number('4272678916515987') == '4272 67** **** 5987'
