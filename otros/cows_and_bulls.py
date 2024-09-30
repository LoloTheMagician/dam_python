import random


def generate_random_number():
    min, max = 0, 9
    return random.randint(min, max)


def is_number(element: str | int | float) -> bool:
    try:
        return isinstance(int(element), int)
    except:
        return False


def valid_lenght(text: str, lenght=4):
    return len(text) == lenght


def cows_bulls():

    random_number = "".join([str(generate_random_number()) for _number in range(4)])
    print(random_number)

    number_guesses = 0
    print("Welcome to the Cows and Bulls Game!")

    while True:

        user_guess = input("Enter a number: ")

        user_guess_is_number = is_number(user_guess)
        if not user_guess_is_number:
            print("No has introducido un número!")
            continue

        valid_number = valid_lenght(user_guess)
        if not valid_number:
            print("No es un número válido!")
            continue

        number_guesses += 1
        number_cows_bulls = {"cows": 0, "bulls": 0}
        for index, digit in enumerate(random_number):
            user_number_digit = user_guess[index]
            if user_number_digit == digit:
                number_cows_bulls["cows"] += 1
                continue
            if user_number_digit in random_number:
                number_cows_bulls["bulls"] += 1
        if number_cows_bulls["cows"] == len(random_number):
            print("Has acertado!")
            print(f"El número era {random_number}")
            return
        for successes in number_cows_bulls.items():
            animal, correct_guesses = successes
            print(f"{animal}: {correct_guesses} ", end="")
        print()


cows_bulls()
