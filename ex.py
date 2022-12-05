
#a = ["a","b","c"]
#b = 1

#for i in a :
#    print(f"{b} Ma lettre : {i} ")
#    b += 1

#-----------------------------------

#for number,i in enumerate(a) :

#    print(f"{number}. Ma lettre : {i} ")

#-----------------------------------

#def mafonction(ami):
 #   print ("salut les amis")


#mafonction("ami")

#-----------------------------------

#import os


#a = os.listdir("C:\\Users")
#b = 1

#for number,i in enumerate(a) :

#    print(f"{number}. Mon dossier : {i} ")

#for i in a :
 #  print(f"{b} Mon dossier : {i} ")
 #  b += 1

#print (a)

#-----------------------------------

import os
import sys 

print(sys.argv[0])
liste = os.listdir("c:\\Users")

for nb, i in enumerate(liste):
    print (f"{nb}.{i}")
print (liste)

#-----------------------------------