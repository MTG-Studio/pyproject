def filter_by_state(dictionary_list: list, state='EXECUTED') -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""
    result_list = []
    for i in dictionary_list:
        if i['state'] == state:
            result_list.append(i)
    return result_list


def sort_by_date(dictionary_list: list, reversed_sort=True) -> list:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_list = sorted(dictionary_list, key=lambda dictionary:
                         dictionary['date'], reverse=reversed_sort)
    return sorted_list
