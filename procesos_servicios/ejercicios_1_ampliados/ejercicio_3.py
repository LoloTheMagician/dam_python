from pal import palabras


def filtrar_palabras(palabras: list[str], n_chars: int):
    return list(filter(lambda palabra: len(palabra) > n_chars, palabras))


print(filtrar_palabras(palabras, 4))


def filtrar_pal(pals: list[str], n: int) -> list[str]:
    min_len_pals = []
    for pal in pals:
        len_pal = len(pal)
        if not (len_pal > n):
            continue
        min_len_pals.append(pal)
    return min_len_pals


print(filtrar_pal(palabras, 4))
