#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)






import sys
import csv

def pr_value(line):
  k = line[1].strip()
  if k != "":
    print("{0}\t{1}".format(k, 1))

if __name__ == "__main__":

  infile = csv.reader(sys.stdin, delimiter=',')
  line = next(infile)

  #go to first line
  if line[0] != "color" and line[1] != "director_name" :
    pr_value(line)

  for line in infile:
	#print 	
    pr_value(line)
