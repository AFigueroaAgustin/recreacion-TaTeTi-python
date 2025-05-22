
# IMPORTACIONES
from equipos import *
from juego import juego
from reporte import informe
from constantes import *
import numpy as np

# ------------- Programa Principal -------------

eq1 = np.empty(DIM, dtype=id_equipo)
eq2 = np.empty(DIM, dtype=id_equipo)
cant_eq1 = 0
# TABLERO
tablero = np.array([
    ["|", "|", "|", ],
    ["|", "|", "|", ],
    ["|", "|", "|"]
])

cant_eq1 = carga_de_eq1(eq1)
carga_de_eq2(cant_eq1, eq2)
cant_jugadas = juego(eq1, eq2, cant_eq1, tablero)
informe(eq1, eq2, cant_eq1, cant_jugadas)
