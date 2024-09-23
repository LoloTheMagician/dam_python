def upper_chars(string: str):
    return len(list(filter(lambda char: char == char.upper(), string)))


print(upper_chars("PePito"))
