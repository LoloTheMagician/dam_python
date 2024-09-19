palabras = ["pepe", "jose", "gonzalo", "alejandro"]


def filtrar_palabras(palabras: list[str], number_words: int) -> list[str] | list[any]:
    palabras_validas = []
    for palabra in palabras:
        len_palabra = len(palabra)
        if len_palabra <= number_words:
            continue
        palabras_validas.append(palabra)
    return palabras_validas


filtrar = lambda palabras, min_len: list(
    filter(lambda pal: len(pal) > min_len, palabras)
)


print(filtrar_palabras(palabras, 4), filtrar(palabras, 4))
