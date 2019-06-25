def imprimirMensaje():
	print('estoy aprendiendo python')
	print('estoy aprendiendo en globant 2')


imprimirMensaje()

#con parametros
# python pasa siempre los parametros por referencia

def sumar(a,b):
		resultado = a + b
		return resultado


variableA=12
variableB=32

print(sumar(variableA,variableB))