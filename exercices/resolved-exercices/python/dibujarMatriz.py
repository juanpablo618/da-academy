def dibujaMatriz(M):
 for i in range(len(M)):
 	print("["),
 for j in range(len(M[i])):
 	print '{:>3s}'.format(str(M[i][j])),
 print("]")

m = [[1,2],[3,4]]

dibujaMatriz(m)