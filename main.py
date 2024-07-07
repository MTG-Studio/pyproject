# from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

# card_number = "4272678916515987"
# print(get_mask_card_number(card_number))

# account_number = "243504759435743295437990090"
# print(get_mask_account(account_number))

# card_type_and_number_1 = "Visa Platinum 7000 7922 8960 6361"
# print(mask_account_card(card_type_and_number_1))

# card_type_and_number_2 = "Счет 73654108430135874305"
# print(mask_account_card(card_type_and_number_2))

# card_type_and_number_3 = "Maestro 1596837868705199"
# print(mask_account_card(card_type_and_number_3))

# date_input = "2024-03-11T02:26:18.671407"
# print(get_date(date_input))

dict_list = [{'id': 41428829,
              'state': 'EXECUTED',
              'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570,
              'state': 'EXECUTED',
              'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727,
              'state': 'CANCELED',
              'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591,
              'state': 'CANCELED',
              'date': '2018-10-14T08:21:33.419441'}]
state_filter = 'CANCELED'

filter_by_state(dict_list, state_filter)
sort_by_date(dict_list)
