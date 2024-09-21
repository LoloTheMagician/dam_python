def media(*numbers):
    sum_numbers = 0
    counter: int = 0
    for number in numbers:  # [1,2,3,4,'pepe',5]
        try:
            number_to_int = int(number)
            sum_numbers += number_to_int
            counter += 1
        except:
            return f"{number} is NOT a valid number"
    result = sum_numbers / counter
    return f"Media of {' + '.join(map(str, numbers))} is {result}"


print(media(1, 2, 3, 4, 5))
