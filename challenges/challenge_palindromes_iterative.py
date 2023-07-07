def is_palindrome_iterative(word: str):
    arr_word = list(word)
    new_word = []
    if word == "":
        return False

    for i in range(len(arr_word) - 1, -1, -1):
        new_word.append(arr_word[i])

    if arr_word == new_word:
        return True

    return False
