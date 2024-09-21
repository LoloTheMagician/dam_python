def lista_palabras():
    numero_palabras = input("Digame el número de palabras que va a introducir: ")
    try:
        numero_palabras = int(numero_palabras)
    except:
        return print(f"No es un número válido")
    if numero_palabras <= 0:
        return print("Número no válido")
    counter = 0
    palabras = []
    while counter < numero_palabras:
        palabra = input("Dime una palabra: ")
        if palabra == "":
            continue
        palabras.append(palabra)
        counter += 1
    for palabra in palabras:
        print(palabra)
    return palabras


def ocurrencias_palabra(palabras: list[str], palabra_encontrar: str):
    return palabras.count(palabra_encontrar)


print(ocurrencias_palabra(lista_palabras(), "pepe"))
