f=3
c=3
matriz=[]

for i in range(f):
	matriz.append([0]*c)

print matriz


contador=1
for i in range(f):
	for j in range(c):
		matriz[i][j]=contador
		contador+=1

print matriz


for i in range(f):
	for j in range(c):
		print j,
	print 