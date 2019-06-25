#Generadores
#Estructuras que extraen valores de una funcion y se almacena en objetos iterables o sea que se pueden recorrer
#se almacenan de a 1 en 1
#son + eficientes que las funciones tradicionales
#muy utiles con listas de valores infinitos (direcciones de ip al azar)

def generaPares(limite):
	num=1
	miLista=[]

	while num<limite:
		yield num*2
		
		num=num+1		

devuelvePares=generaPares(10)

print(next(devuelvePares))

print("otra linea de codigo, generador entra en suspension")

print(next(devuelvePares))