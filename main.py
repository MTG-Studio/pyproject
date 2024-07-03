from src.widget import mask_account_card
from src.widget import get_date


# card_number = "4272678916515987"
# print(get_mask_card_number(card_number))

# account_number = "243504759435743295437990090"
# print(get_mask_account(account_number))

card_type_and_number_1 = "Visa Platinum 7000 7922 8960 6361"
print(mask_account_card(card_type_and_number_1))

card_type_and_number_2 = "Счет 73654108430135874305"
print(mask_account_card(card_type_and_number_2))

card_type_and_number_3 = "Maestro 1596837868705199"
print(mask_account_card(card_type_and_number_3))

date_input = "2024-03-11T02:26:18.671407"
print(get_date(date_input))
