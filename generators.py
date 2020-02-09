# son funciones que general un opjeto iterable, el cual va devolviendo 1 valor a la vez por cada llamada
# muy itules para generar solo los valores necesarios, y no tener que generar el array completo

def generaPares(limite):

    num=1

    while num < limite:

        yield num*2 #yield devuelve el valor del objeto iterable  >> y se multiplica x2

        num=num+1

devuelvePares=generaPares(25)  #es necesario ena variable obj donde almacenar el obj iterable

#for i in devuelvePares:  #es necesario el for (o while) para recorrer el obj iterable

 #   print(i)
#de esta forma la funcion esta devolviendo e imprimiendo todos los valores, lo cual no tiene mucha diferencia de una funcion comun

print(next(devuelvePares))

print('mas codigo')

print(next(devuelvePares))

print('mas codigo')

print(next(devuelvePares))

#de esta forma es mas eficiente, ya que solo genera lo q necesita



