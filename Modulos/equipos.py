

# TODO: Se encarga de cargar los datos del equipo N°1
def carga_de_eq1(v):
    b = 0
    print("--------- El equipo N°1 ---------")
    cant = int(input("ingrese la cantidada de jugadores que tendra el equipo N°1: "))
    while b == 0:
        if cant < 2 or cant > 10:
            print("la cantidad ingresada es insuficiente.")
            print("Vuelva a ingresar la cantiada.")
            cant = int(input("ingrese la cantidada de jugadores: "))
        else:
            print("cantidad ingresada correctamente.")
            b = 1
    for i in range(cant):
        b1 = 0
        if i > 0:
            print("--------- El equipo N°1 ---------")
        v[i]["id_jugador"] = int(input("ingrese el ID del juegador (tiene que ser de 3 cifras) : "))
        while b1 == 0:
            if v[i]["id_jugador"] < 100 or v[i]["id_jugador"] > 999:
                print("Vuelva a ingresar el ID.")
                v[i]["id_jugador"] = int(input("ingrese el ID del juegador: "))
            else:
                b1 = 1
            v[i]["nomapo"] = input("ingrese el nombre o el apodo del jugador: ").title()
            v[i]["pt"] = 0

    return cant


# TODO: Se encarga de cargar los datos del equipo N°2
def carga_de_eq2(d, v):
    for i in range(d):
        b1 = 0
        print("--------- El equipo N°2 ---------")
        print(f"El equipo tendra la cantidad de {d} que es la misma cantidad del equipo N°1. ")
        v[i]["id_jugador"] = int(input("ingrese el ID del juegador (tiene que ser de 3 cifras) : "))
        while b1 == 0:
            if v[i]["id_jugador"] < 100 or v[i]["id_jugador"] > 999:
                print("Vuelva a ingresar el ID.")
                v[i]["id_jugador"] = int(input("ingrese el ID del juegador: "))
            else:
                b1 = 1
        v[i]["nomapo"] = input("ingrese el nombre o el apodo del jugador: ").title()
        v[i]["pt"] = 0
