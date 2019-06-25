#!/usr/bin/python

import urllib2
import sys
import argparse

# http://i3.ytimg.com/vi/J---aiyznGQ/
#baseUrl= 'http://i3.ytimg.com/vi/J---aiyznGQ/'

CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--lista",  # name on the CLI - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  type=str,
  default=[1, 2, 3],  # default if nothing is provided
)

args = CLI.parse_args()

filedata = urllib2.urlopen(args.lista[0]+args.lista[2])  
datatowrite = filedata.read()

# downloadAFile

for i in range(2,4):
    print(i)
    with open('/home/developer/work/da-academy/exercices/resolved-exercices/hadoop/'+args.lista[1]+'/'+args.lista[i], 'wb') as f:  
        f.write(datatowrite)


