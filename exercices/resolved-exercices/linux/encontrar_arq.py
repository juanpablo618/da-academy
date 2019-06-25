#!/usr/bin/python
import os, sys
from stat import *
 
def walktree(top, callback):
   '''recursively descend the directory tree rooted at top,
      calling the callback function for each regular file'''
 
   for f in os.listdir(top):
       pathname = os.path.join(top, f)
       mode = os.stat(pathname)[ST_MODE]
       if S_ISDIR(mode):
           # It's a directory, recurse into it
           walktree(pathname, callback)
       elif S_ISREG(mode):
           # It's a file, call the callback function
           callback(pathname,f,top)
       else:
           # Unknown file type, print a message
           print 'Skipping %s' % pathname
 
def visitfile(fullname,file,path):
   print 'visiting', file, 'in', path, "=", fullname
 

if __name__ == '/home/developer/work':
   print(walktree(sys.argv[1], visitfile))