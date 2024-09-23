palabras = ["pepe", "juan", "jose", "manuel", "", 5, "Carlitos"]


def truthy(element: any):
    return element


def is_int(element: int | str):
    return isinstance(element, int)


def mas_larga(palabras: list[str]):
    mas_larga_palabra = ""
    for pal in palabras:
        pal_exist = truthy(pal)
        if not pal_exist:
            continue
        pal_is_int = is_int(pal)
        if pal_is_int:
            continue
        len_pal, len_pal_larga = len(pal), len(mas_larga_palabra)
        if len_pal > len_pal_larga:
            mas_larga_palabra = pal
    return mas_larga_palabra


print(mas_larga(palabras))


def is_str(elem: any):
    return isinstance(elem, str)


def exist(elem: str):
    return elem


def larga(palabras: list[str]):
    return list(
        sorted(map(lambda pal: (len(pal), pal), filter(lambda pal: is_str(pal) and exist(pal), palabras)))[::-1][0]
    )[1]


print(larga(palabras))
