def to_lowcase(text: str):
    return text.lower()


def is_vowels(char: str):
    return char in "aeiou"


def contar_vocales(string: str):
    return len(list(filter(lambda char: is_vowels(to_lowcase(char)), string)))


print(contar_vocales("GonzalO"))


def many_vowels(string: str):
    just_vowels = [char for char in string if char.lower() in "aeiou"]
    return len(just_vowels)


print(many_vowels("GonzalO"))


def count_vowels(string: str):
    vowels = "aeiou"
    counter = 0
    for char in string:
        char_lower = char.lower()
        if char_lower not in vowels:
            continue
        counter += 1
    return counter


print(count_vowels("GonzalO"))
