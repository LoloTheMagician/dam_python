def many_upper_chars(word: str) -> int:
    counter = 0
    for char in word:
        if char == char.upper():
            counter += 1
    return counter


def upper_chars(word: str) -> int:
    return len(list(filter(lambda char: char == char.upper(), word)))


print(many_upper_chars("PepEEe"), upper_chars("PepE"))
