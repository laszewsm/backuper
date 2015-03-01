#!/usr/bin/env python
import os
import os.path
import subprocess as sub
import zipfile

import time
import datetime


print ("ZATTO BACKUP ver.0.0.1")



# To add folder change lok1, lok2 on /my/destination

zf = zipfile.ZipFile("backup.zip", "w")
for dirname, subdirs, files in os.walk("/home"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()
print ("Completed")
	

#MySQL login 

DB_HOST = 'host'
DB_USER = 'user'
DB_USER_PASSWORD = 'password'
DB_NAME = 'name'
BACKUP_PATH = '/root/backuper'




PATH = BACKUP_PATH 

# Checking if backup folder already exists or not. If not exists will create it.
print "creating backup folder"
if not os.path.exists(PATH):
    os.makedirs(PATH)

# Code for checking if you want to take single database backup or assinged multiple backups in DB_NAME.
print "checking for databases names file."
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print "Databases file found..."
    print "Starting backup of all dbs listed in file " + DB_NAME
else:
    print "Databases file not found..."
    print "Starting backup of database " + DB_NAME
    multi = 0

# Starting actual database backup process.
if multi:
   in_file = open(DB_NAME,"r")
   flength = len(in_file.readlines())
   in_file.close()
   p = 1
   dbfile = open(DB_NAME,"r")

   while p <= flength:
       db = dbfile.readline()   # reading database name from file
       db = db[:-1]         # deletes extra line
       dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + PATH + "/" + db + ".sql"
       os.system(dumpcmd)
       p = p + 1
   dbfile.close()
else:
   db = DB_NAME
   dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + PATH + "/" + db + ".sql"
   os.system(dumpcmd)

print "Backup script completed"
print "Your backups has been created in '" + PATH + "' directory"


 

#subprocess.call("mv /root/backup.zip /root/
