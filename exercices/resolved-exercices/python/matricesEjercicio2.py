def dibujaMatriz(M):
 for i in range(len(M)):
 	print("["),
 	for j in range(len(M[i])):
 		print '{:>3s}'.format(str(M[i][j])),
  	print("]")


m = [[1,2],[3,4]]
p = [[1,2],[3,4,3]]

print("dibujando matriz m:")
dibujaMatriz(m)

print("")
print("matriz 3 x 3 llamada n")
print("")
n = [[1,10,100], [20,2,200],[300,30,3]]

dibujaMatriz(n)
print("")

def creaMatriz(n,m):
	 '''
	 Esta funcion crea una matriz vacia con n filas y n columnas.
	 @param n : Nro de filas.
	 @param m : Nro de columnas
	 @type n: int
	 @type m: int
	 @return: devuelve una matriz n por m
	 @rtype: matriz (lista de listas)
	 '''
	 matriz = []
	 for i in range(n):
	 	a = [0]*m
	 	matriz.append(a)
	 return matriz

def matrizCorrecta(M):
	 '''
	 Nos dice si una matriz es correcta.
	 @param M: una matriz
	 @type M: matriz
	 @return: True si es correcta, False en caso contrario
	 '''
	 filas = len(M)
	 columnas = len(M[0])
	 correcto = True
	 i = 1
	 while i < filas and correcto:
	 	correcto = (len(M[i]) == columnas)
	 	i += 1
	 return correcto


def filas(M):
 '''
 Nos dice el nro de filas de una matriz correcta.
 @param M: una matriz
 @type M: matriz
 @return: nro de filas
 '''
 if matrizCorrecta(M):
 	return len(M)

def columnas(M):
 '''
 Nos dice el nro de columnas de una matriz correcta.
 @param M: una matriz
 @type M: matriz
 @return: nro de columnas
 '''
 if matrizCorrecta(M):
 	return len(M[0])

def matrizIdentidad(n):
 '''
 Crea una matriz identidad de tamano n
 @param n : nro de filas.
 @type n : entero
 @return: matriz identidad de tamano n
 '''
 m = creaMatriz(n,n)
 for i in range(n):
 	m[i][i] = 1
 return m

def copy(m):
 '''
 Realiza una copia independiente de la matriz
 '''
 result=[]
 for f in m:
 	result.append(f[:])
 return result

print("cantidad de columnas de m")
print(columnas(m))

def matrizIdentidad(n):
	'''
	Crea una matriz identidad de tamano n
	@param n : nro de filas.
	@type n : entero
	@return: matriz identidad de tamano n
	'''
	m = creaMatriz(n,n)
	for i in range(n):
		m[i][i] = 1
	return m

	def copy(m):
		'''
		Realiza una copia independiente de la matriz
		'''
		result=[]
		for f in m:
			result.append(f[:])
		return result

def sumaMatriz(A,B):
	'''
	Suma dos matrices. Las dos matrices deben ser de la misma dimension
	@param A: una matriz nxm
	@param B: una matriz nxm
	@type A: Matriz
	@type B: Matriz
	@return: Matriz suma
	'''
	if filas(A) == filas(B) and columnas(A) == columnas(B):
		C = creaMatriz(filas(A), columnas(A))
		for i in range(filas(A)):
			for j in range(columnas(A)):
				C[i][j] = A[i][j] + B[i][j]
		return C



def multiplicaMatriz(A,B):
	'''
	Multiplica dos matrices. El nro de columnas de la primera debe ser igual al nro de filas de la segunda.
	@param A: una matriz nxm
	@param B: una matriz mxk
	@type A: Matriz
	@type B: Matriz
	@return: Matriz multiplicacion nxk
	'''
	if columnas(A) == filas(B):
		C = creaMatriz(filas(A), columnas(B))
		for i in range(filas(C)):
			for j in range(columnas(C)):
				for k in range(columnas(A)):
					C[i][j] += A[i][k] * B[k][j]
		return C


def traspuesta(M):
	'''
	Calcula la matriz traspuesta de M
	'''
	m = len(M) #filas
	n = len(M[0]) # columnas
	T = creaMatriz(m,n)
	for i in range(n):
		for j in range(m):
			T[i][j] = M[j][i]
	return T

print("")
print("transpuesta de m:")
print(traspuesta(m))

def combinacion(m,i,j,e):
	'''
	Combina las filas i y j, agregando a la fila j el producto de la fila i por un factor e
	'''
	n=len(m)
	for c in range(n):
		m[j][c]=m[j][c]+e*m[i][c]


def intercambiaFilas(m,i,j):
	m[i],m[j] = m[j],m[i]


def multiplicaFila(m,f,e):
	'''
	Multiplica la fila f por el valor e
	'''
	n=len(m)
	for c in range(n):
		m[f][c]=m[f][c]*e


def primeroNoNulo(m,i):
	'''
	A partir de la fila i, busca la primera fila j cuya entrada
	(i,j) es nula
	'''
	result=i
	while result<len(m) and m[result][i]==0:
		result=result+1
	return result


def determinante(matriz):
	'''
	Calcula el determinante poniendo ceros debajo
	de la diagonal principal
	'''
	m = copy(matriz)
	n=len(m)
	det=1
	for i in range(n):
		j=primeroNoNulo(m,i)
		if j == n:
			return 0
		if i!=j:
			det=-1*det
			intercambiaFilas(m,i,j)
		det=det*m[i][i]
		multiplicaFila(m,i,1./m[i][i])
		for k in range(i+1,n):
			combinacion(m,i,k,-m[k][i])
	return det

print("")
print("matriz m:")
print(m)
print("")
print("determinante:")
print(determinante(m))

print("")
print("matrices multiplication")
j =[[1,2,-3],[4,0,-2]]
u =[[3,1],[2,4],[-1,5]]

print(multiplicaMatriz(j,u))

print("")
print("invertir matrices")
print("en el metodo de gaussJordan en el archivo gaussJordan.py")

g =[[3,1,3,1],[2,4,3,1],[-1,5,3,1]]
print("determinante de una 4 x 4 ")
print(g)
print(determinante(g))

def obtainMatrixRow(matriz, row):
	if matrizCorrecta(matriz):
		for i in range(filas(matriz)):
				if i == row:
					for j in range(len(matriz[i])):
						print(matriz[i][j])	
			

def obtainMatrixColumn(matriz, column):
	print(columnas(matriz))
	if matrizCorrecta(matriz):
		for i in range(columnas(matriz)):
				if i == column:
					for j in range(len(matriz[i])):
						print(matriz[i][j])	

print("test de funcion q devuelve fila especifica")
obtainMatrixRow(j,1)

print("test de la funcion q devuelve columna especifica")
obtainMatrixColumn(j,1)



