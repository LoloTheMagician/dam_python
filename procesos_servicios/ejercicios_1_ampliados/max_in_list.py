numbers = [1, 2, 3, 4, 5]


def get_max_number(numbers: list[int]) -> int:
    return max(numbers)


print(get_max_number(numbers))


def get_max(numbers: list[int]):
    # Almacenar número más grande
    greater_number = 0
    for number in numbers:
        # Asegurarse que es de tipo integer
        if not isinstance(number, int):
            continue
        # Evaluar número más grande
        if greater_number < number:
            greater_number = number
    return greater_number


print(get_max([1, 2, 3, 4, "pepe", 5]))

# Función Lambda en una línea con la función built in max
max_number = lambda numbers: max(numbers)

print(max_number(numbers))


def sort_numbers(numbers: list[int]) -> int:
    return sorted(numbers, reverse=True)[0]


print(sort_numbers(numbers))
