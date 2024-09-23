numbers = [1, 2, 3, 4, 5, 6]


def max_number(numbers: list[int]):
    return max(numbers)


# print(max_number(numbers))


def max_number_by_sort(numbers: list[int]):
    return sorted(numbers)[-1]


# print(max_number_by_sort(numbers))


def max_number_validations(*numbers: str):
    valid_numbers = [
        integer_element or element
        for element in numbers
        if (integer_element := "")
        or isinstance(element, int)
        or (
            isinstance(element, str)
            and element.isnumeric()
            and (integer_element := int(element))
        )
    ]
    return valid_numbers


print(max_number_validations(*numbers, *["pepe", "juan", 7, "8"]))
