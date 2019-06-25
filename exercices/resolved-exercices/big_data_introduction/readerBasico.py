# /home/developer/Downloads/movie_metadata.csv
import csv, operator

csvarchivo = csv.reader(open('/home/developer/Downloads/movie_metadata.csv'))
listaordenada = sorted(csvarchivo, 
                       key=operator.itemgetter(2), 
                       reverse=False)
print(listaordenada)