def to_format(number: int | float, number_decimals: int):
    return f"{number:.{number_decimals}f}"


def calculate_media(sum_numbers: int | float, number_of_numbers: int) -> str:
    media = sum_numbers / number_of_numbers
    format_media = to_format(media, number_decimals=2)
    return format_media


def main():
    sum_numbers = 0
    valid_numbers = 0
    print("To STOP just ENTER")
    while True:
        user_input = input("Give me a Number : ")
        if user_input == "":
            print("Let's calculate the Media!")
            break
        try:
            sum_numbers += int(user_input)
            valid_numbers += 1
        except:
            continue
    if valid_numbers <= 0:
        return "Not able to calculate..."
    result = calculate_media(sum_numbers, valid_numbers)
    return f"Media is {result}"


print(main())
