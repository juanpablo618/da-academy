# La mas sencilla e intuitiva
def crearMatriz(numero_filas, numero_columnas):
	matriz = [list(range(numero_columnas)) for i in list(range(numero_filas))]
	return matriz

def pedirTamano():
	try:
		numero_filas = int(input("cantidad de filas "))
	except:
		print('ingrese solo nros')

	try:
		numero_columnas = int(input("cantidad de columnas "))

	except:
		print('ingrese solo nros')

	return(crearMatriz(numero_filas,numero_columnas))


def sumarMatrizEstatica():
	pedirTamanoYSumarMatriz()


print(pedirTamano())
