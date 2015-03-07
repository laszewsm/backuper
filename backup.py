#!/usr/bin/env python
''' W celu poprawniego dzialania ponizszego skryptu, trzeba skonigurowac 
logowanie RSA / DSA na maszynie na ktora, bedziemy przenosic nasza kopie zapasowa. Sposob konfiguracji mozna znalezc tutaj 
http://www.nerdokracja.pl/linux-logowanie-ssh-klucze-rsa/
 
'''
import os
import os.path

print ('Tworzenie folderu tymczasowego')

cmd = "mkdir ~/tmp"  #Tworzenie folderu tymczasowego 

print ('Tworze kopie zapasowa bazy danych')

# -u user << wpisujemy swoj login 
# -phaslo << haslo wpisujemy ciagiem zaraz po -p
# moja_baza_danych << nalezy zmienic na nazwe bazy danych do zachowania
# moja.sql << nazwa npliku .sql z baza danych 

cmd1 = "mysqldump -u user -phaslo moja_baza_dancyh >  ~/tmp/moja.sql"

print ('Tworze kopie zapasa folderow')

# /home/ /root/ /var/www/ /etc/ << foldery do zachowania mozna zmieniac wedle uznania 

cmd2 = "zip -r ~/tmp/backup.zip  ~/tmp/moja.sql /home/ /root/ /var/www/ /etc/"

# Logowanie za pomoca scp
# konto << nazwa konta na maszynie do ktorej backup.zip bedzie wyslany 
# jakis_adres_ip << adres maszyny na ktora backup bedzie wyslany
# /home/backup/ << miejsce gdzie backup.zip bedzie przechowywany 

print ('Wysylanie backupu ...')

cmd3 = "scp ~/tmp/backup.zip konto@jakis_aders_ip:/home/backup"

print('Usuniecie folderu tymczasowego')

cmd4 = "rm -R ~/tmp"

#wykonianie zdefiniowanych wczesniej polecen 

os.system(cmd)
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
os.system(cmd4)




