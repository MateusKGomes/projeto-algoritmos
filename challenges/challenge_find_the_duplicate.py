def find_duplicate(nums: list):
    ordered = sorted(nums)
    for num in range(0, len(ordered) - 1):
        if not isinstance(ordered[num], int) or ordered[num] < 0:
            return False
        if ordered[num] == ordered[num + 1]:
            return ordered[num]
    return False
