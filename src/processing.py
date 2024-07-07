def filter_by_state(dictionary_list, state='EXECUTED'):
    result_list = []
    for i in dictionary_list:
        if i['state'] == state:
            result_list.append(i)
    print(result_list)


def sort_by_date(dictionary_list, reversed_sort=True):
    sorted_list = sorted(dictionary_list, key=lambda dictionary:
                         dictionary['date'], reverse=reversed_sort)
    print(sorted_list)
