from utils.order import merge_sort


def is_anagram(first_string: str, second_string: str):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first = list(first_string.lower())
    second = list(second_string.lower())

    ordered_first = merge_sort(first)
    ordered_second = merge_sort(second)

    if ordered_first == ordered_second:
        return ("".join(ordered_first), "".join(ordered_second), True)

    return ("".join(ordered_first), "".join(ordered_second), False)
