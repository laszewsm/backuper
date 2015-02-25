#!/usr/bin/env python
import os
import os.path
import subprocess as sub
#from zipfile_infolist import print_info
import zipfile

print ("ZATTO BACKUP ver.0.0.1")

##############################################
#  Tu definujemy foldery do z zipowania      #
##############################################


zf = zipfile.ZipFile('/root/test/testowy.txt', 'w')
try:
	print ('tworze archiwum')
	zf.write('backup.zip')
finally:
	print ('zakonczono')
	zf.close()
print
print_info('backup.zip')
