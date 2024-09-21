def main():
    ask_numbers = input("Escribe dos números: ")
    list_numbers = ask_numbers.split()
    if len(list_numbers) != 2:
        return "Contenido inválido..."
    valid_numbers = []
    for number in list_numbers:
        try:
            valid_numbers.append(int(number))
        except:
            print(f"{number} no es un número valido")
            return
    min_number, max_number = sorted(valid_numbers)
    for number in range(min_number, (max_number + 1)):
        if number % 2 == 0:
            print(number)


main()
