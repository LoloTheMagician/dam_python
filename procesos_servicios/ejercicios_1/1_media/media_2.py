def main():
    sum_numbers = 0
    valid_numbers = 0
    while True:
        user_input = input("Give me a Number : ")
        if user_input == "":
            break
        try:
            sum_numbers += int(user_input)
            valid_numbers += 1
        except:
            continue
    result = sum_numbers / valid_numbers
    return f"Media is {result}"


print(main())
