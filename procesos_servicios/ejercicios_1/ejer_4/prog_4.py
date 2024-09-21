from enum import Enum


def is_number(possible_number: str | int | float) -> bool:
    try:
        return isinstance(int(possible_number), int)
    except:
        return False


def is_par(number: int) -> bool:
    return number % 2 == 0


class NUMBER_TYPE(Enum):
    PAR = "par"
    IMPAR = "impar"


def input_ask_number_type(par_impar: NUMBER_TYPE):
    return f"Introduce un número {par_impar}:"


def number_type_input(number_type: NUMBER_TYPE) -> tuple[bool, str]:
    number_type = number_type.value
    user_input = input(input_ask_number_type(number_type))
    input_is_number = is_number(user_input)
    if not input_is_number:
        return (False, f"{user_input} NO es un número, ergo, NO es {number_type}")
    number_is_par = is_par(number := int(user_input))
    if number_type == NUMBER_TYPE.IMPAR.value:
        number_is_par = not number_is_par
    if not number_is_par:
        return (False, f"{number} NO es un número {number_type}")
    return (True, f"Bien!, {number} es {number_type}")


def main() -> str:
    par_number = number_type_input(NUMBER_TYPE.PAR)
    is_valid_par, text_log_par = par_number
    if not is_valid_par:
        return text_log_par
    else:
        print(text_log_par)
    impar_number = number_type_input(NUMBER_TYPE.IMPAR)
    is_valid_impar, text_log_impar = impar_number
    if not is_valid_impar:
        return text_log_impar
    return text_log_impar


print(main())
