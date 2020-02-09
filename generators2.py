#basicamente es para acceder o manejar array anidados

def devuelveCiudades (*ciudades):
    for elemento in ciudades:

        #for subElemento in elemento:
            yield from elemento


ciudadesDevueltas = devuelveCiudades("Caracas", "Madrid", "Buenos Aires")

print(next(ciudadesDevueltas))

print(next(ciudadesDevueltas))