#!/usr/bin/python

import urllib2

filedata = urllib2.urlopen('https://github.com/aatishnn/lszip/blob/master/test_files/test_file.zip')  
datatowrite = filedata.read()

with open('/home/developer/work/da-academy/exercices/resolved-exercices/hadoop/downloadAFile/test_file.zip', 'wb') as f:  
    f.write(datatowrite)