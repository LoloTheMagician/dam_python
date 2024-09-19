from utils.log import log

# Prog1: Escriba un programa que pida dos números y que escriba su media aritmética.


# First way -> straight forward
def media_aritmetica(a: int, b: int) -> int | float:
    return (a + b) / 2


# Second way -> edge cases


def ask_user_input(text: str) -> str:
    return input(text)


def is_number(a) -> bool:
    try:
        return int(a)
    except:
        return False


def division(a, b):
    return a / b


def media(
    *numbers: list[int | float],
) -> int | float:
    sum_numbers = sum(numbers)
    division_media = division(sum_numbers, len(numbers))
    return division_media


def is_invalid_text(not_number: str):
    return f"{not_number} is not a number"


def main():

    ask_for_number = "Give me a number: "

    first_number: str = ask_user_input(ask_for_number)
    first_is_valid_number: bool = is_number(first_number)

    if not first_is_valid_number:
        invalid_number = is_invalid_text(first_number)
        return invalid_number

    second_number: str = ask_user_input(ask_for_number)
    second_is_valid_number: bool = is_number(second_number)

    if not second_is_valid_number:
        invalid_number = is_invalid_text(second_number)
        return invalid_number

    media_numbers = media(int(first_number), int(second_number))
    return f"Media of {first_number} and {second_number} is {media_numbers}"


log(media_aritmetica(2, 4), main())
