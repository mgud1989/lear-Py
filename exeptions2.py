def evaluaEdad(edad):
    if edad<0:
        raise TypeError("Nadie puede tener edad negativa") #raise para lanzar exeptions propias
    if edad<20:
        return "joven"
    elif edad<40:
        return "maduro"
    elif edad<80:
        return "grande"
    elif edad<100:
        return "cuidate"

try:
    print(evaluaEdad(-45))
except TypeError as ErrorDeNumeroNegativo: #capturo el error, continuando con la ejecucion y mostrando un msj mas descriptivo

    print ("No existen edades negativas")

print ("Programa finalizado")