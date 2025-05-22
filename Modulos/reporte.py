
#Todo:Realiza un reporte de la partida jugada
def informe(eq1, eq2, d, j):
    print(f" JUGADAS: {j:<30}")
    print(f" {"Equipo N°1":<15} {"Equipo N°2":<15}")
    sum_eq1 = 0
    sum_eq2 = 0
    for i in range(d):
        print(f"{eq1[i]["nomapo"]:<10} {eq1[i]["pt"]:<2} {"|":<2} {eq2[i]["nomapo"]:<10} {eq2[i]["pt"]:<7}")
        sum_eq1 = eq1[i]["pt"] + sum_eq1
        sum_eq2 = eq2[i]["pt"] + sum_eq2
    print("")
    print(f"total:{sum_eq1:<10} {sum_eq1:<2} {"|":<2} {sum_eq2:<2}")
    if sum_eq1 > sum_eq2:
        print(f"{"Ganador: Equipo N°1 ":<10} ")
    else:
        print(f"{"Ganador: Equipo N°2 ":<10} ")
