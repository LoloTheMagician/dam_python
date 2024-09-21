def divisores():
    numero = input("Introduce un número: ")
    try:
        numero = int(numero)
    except:
        return print(f"{numero} no es un número!")
    if numero < 2:
        print("número no suficientemente grande")
        return
    for n_anterior in range(2, numero):
        if numero % n_anterior == 0:
            print(n_anterior)


divisores()
