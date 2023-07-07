def is_palindrome_iterative(word: str):
    reverse_word = list(word).reverse()

    if word == "".join(reverse_word):
        return True

    return reverse_word


print(is_palindrome_iterative("olá"))
