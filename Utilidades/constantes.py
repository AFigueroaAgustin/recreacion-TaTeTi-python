import numpy as np
# formato de los equipos
DIM = 10
id_equipo = np.dtype([
    ("id_jugador", int),
    ("nomapo", "U20"),
    ("pt", int)])