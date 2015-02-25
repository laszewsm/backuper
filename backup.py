#!/usr/bin/env python
import os
import os.path
import subprocess as sub
import zipfile

print ("ZATTO BACKUP ver.0.0.1")


# To add folder change lok1, lok2 on /my/destination

zf = zipfile.ZipFile("myzipfile.zip", "w")
for dirname, subdirs, files in os.walk("/home"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()
print ("Completed")
	

