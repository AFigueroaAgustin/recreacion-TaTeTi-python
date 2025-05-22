import random

# Inicio del juego
# TODO: Se encargara de llevar el control de las jugadas
def jugada(tb, fi):
    valido = False
    while valido == False:
        i = int(input("ingrese la posicion de la fila donde desea poner la ficha: "))
        j = int(input("ingrese la posicion de la columna donde desea poner la ficha: "))
        if tb[i - 1][j - 1] != "|":
            print("Esa posicion ya esta ocupada.")
        else:
            tb[i - 1][j - 1] = fi
            valido = True
    return tb


# TODO: verifica si hay un ganador o empate o lugar en el tablero
def validar_tateti(tb):
    # en comun (0,0)
    if ((tb[0][0] == tb[1][0] == tb[2][0]) or (tb[0][0] == tb[0][1] == tb[0][2])) and tb[0][0] != "|":
        return tb[0][0]
    # en comun (1,1)
    elif ((tb[0][0] == tb[1][1] == tb[2][2]) or (tb[2][0] == tb[1][1] == tb[0][2]) or
          (tb[0][1] == tb[1][1] == tb[2][1]) or (tb[1][0] == tb[1][1] == tb[1][2])) and tb[1][1] != "|":
        return tb[1][1]
    # en comun (2,2)
    elif ((tb[0][2] == tb[1][2] == tb[2][2]) or (tb[2][0] == tb[2][1] == tb[2][2])) and tb[2][2] != "|":
        return tb[2][2]

    # Verificar si el tablero está lleno sin que haya ganador
    for f in tb:
        if "|" in f:
            return "L"  # Hay lugar disponible, el juego no ha terminado.

    return "Empate"  # Si no hay más espacios y no hay ganador, es empate.


def mostrar_tablero(tb):
    for i in range(3):
        for j in range(3):
            print(tb[i][j], end=" ")
        print()

    # MANEJOS DE TURNO


def reiniciar_tablero(tb):
    for i in range(3):
        for j in range(3):
            tb[i][j] = "|"
    return tb  # Tablero vacío


def juego(eq1, eq2, d, tb):
    cont_judadores = 0
    num_par = 0
    # Bucle de cada jugador
    while cont_judadores < d:
        reiniciar_tablero(tb)
        id_j1 = eq1[cont_judadores]["id_jugador"]
        id_j2 = eq2[cont_judadores]["id_jugador"]

        cont_j1 = 0
        cont_j2 = 0
        intentos = 0  # Contador de intentos (máximo 3)
        max_intentos = 3
        turno = "X"
        sigue_jugando = "L"
        dado = random.randint(1, 2)

        # Asignar quién empieza
        if dado == 1:
            f1 = "X"
            f2 = "O"
            print(" ")
            print("Empieza el equipo N°1")
            print("El equipo N°1 son las X y el equipo N°2 son los O")
        else:
            f2 = "X"
            f1 = "O"
            print(" ")
            print("Empieza el equipo N°2")
            print("El equipo N°1 son los O y el equipo N°2 son las X")

        print(id_j1, id_j2)

        # -------- Bucle del juego --------
        while intentos < max_intentos and sigue_jugando == "L":
            mostrar_tablero(tb)

            # Bucle para las jugadas de una partida
            while sigue_jugando == "L":
                if turno == f1:
                    print("Turno del jugador N°1")
                    tb = jugada(tb, f1)
                    cont_j1 += 1
                else:
                    print("Turno del jugador N°2")
                    tb = jugada(tb, f2)
                    cont_j2 += 1

                mostrar_tablero(tb)

                # Validar el estado del juego después de cada jugada
                sigue_jugando = validar_tateti(tb)

                # Cambiar turno
                if sigue_jugando == "L":
                    if turno == "X":
                        turno = "O"
                    else:
                        turno = "X"
            # Resultado de la partida
            if sigue_jugando == "Empate":
                intentos += 1
                int_res = max_intentos - intentos
                print(" ")
                print(f"Empate. Intentos restantes: {int_res}")
                if intentos < max_intentos:
                    tb = reiniciar_tablero(tb)  # Reiniciar el tablero para una nueva partida
                    sigue_jugando = "L"  # Restablecer estado de juego
            elif sigue_jugando != "L":  # Muestra el ganador
                if dado == 1 and sigue_jugando == "X":
                    print(f"Ganador: {id_j1}")
                    eq1[cont_judadores]["pt"] = cont_j1
                else:
                    print(f"Ganador: {id_j2}")
                    eq2[cont_judadores]["pt"] = cont_j2
                cont_judadores += 1
                intentos = max_intentos  # Finalizar bucle del juego

        # Verifica si ya jugaron mas de 3 veces y empataron
        if intentos == max_intentos and sigue_jugando == "Empate":
            print("Se alcanzó el límite de intentos. Fin del juego.")
            eq1[cont_judadores]["pt"] = 1
            eq2[cont_judadores]["pt"] = 1
            cont_judadores += 1
        else:
            num_par += 1
            print("Número de partidas jugadas:", num_par)
    return num_par
