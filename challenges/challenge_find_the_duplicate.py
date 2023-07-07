from challenges.utils.order import merge_sort


def find_duplicate(nums):
    ordered = merge_sort(nums)
    for num in range(0, len(ordered) - 1):
        if not isinstance(ordered[num], int) or ordered[num] < 0:
            return False
        if ordered[num] == ordered[num + 1]:
            return ordered[num]
    return False
