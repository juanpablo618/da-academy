import sys

for line in sys.stdin:
    line = line.strip()
    palabras = line.split()
    for palabra in palabras:
        print '%s\t%s' % (palabra, 1)
