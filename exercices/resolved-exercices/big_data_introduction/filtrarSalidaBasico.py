# /home/developer/Downloads/movie_metadata.csv

import csv, operator

with open('/home/developer/Downloads/movie_metadata.csv') as csvarchivo:
    entrada = csv.DictReader(csvarchivo)
    for reg in entrada:
        print(reg['director_name'], reg['movie_title'])