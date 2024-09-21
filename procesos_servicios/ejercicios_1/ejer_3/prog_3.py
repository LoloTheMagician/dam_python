def is_number(element: int | str):
    try:
        if int(element):
            return True
    except:
        return False


def is_par(number: int):
    return number % 2 == 0


def main():
    par_number = input("Introduce un número par: ")
    impar_number = input("Introduce un número impar: ")
    numbers: dict[str, dict[str, int | bool]] = {
        "par": {"number": par_number, "is_par": True},
        "impar": {"number": impar_number, "is_par": False},
    }
    for number_type, number_info in numbers.items():
        number, has_to_be_par = number_info.values()
        is_a_number = is_number(number)
        if not is_a_number:
            return f"{number} No es un número, ergo, {number} no es un número {number_type}"
        number_is_par = is_par((number := int(number)))
        if number_is_par == has_to_be_par:
            print(f"{number} is correctly typed, is a {number_type.upper()} number")
        else:
            return f"{number} is NOT correctly typed, is NOT a {number_type.upper()} number"


print(main())
