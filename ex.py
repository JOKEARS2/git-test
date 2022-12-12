
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

#import os
#import sys 

#print(sys.argv[0])
#liste = os.listdir("c:\\Users")

#for nb, i in enumerate(liste):
#    print (f"{nb}.{i}")
#print (liste)

#-----------------------------------
#import os
#import sys


#directory_input, mon_prenom, age = sys.argv[1], sys.argv[2], sys.argv[3]

#print(f"path : {directory_input}, mon prenom: {mon_prenom}, mon age :  {age}")

#list_dir = os.listdir(directory_input)


#for number, directory in enumerate(list_dir):
#    print(f"{number}. : {directory}")
#print(f"Le contenu de mon répertoire : {list_dir}")


#-----------------------------------
# import os
# import sys

# directory_input = sys.argv[1]

# print(f"path : {directory_input}")


# with open(directory_input, "a") as f:
#     f.write ("Hello World\n")
#     f.write ("Hello World\n")
#     f.write ("Hello World\n")

#-----------------------------------


# #ouvrir base_eleve, result.txt

# import os
# import sys

# directory_input1, directory_input2 = sys.argv[1], sys.argv[2]
# print(f"path : {directory_input1}")
# print(f"path : {directory_input2}")

 

# with open(directory_input1, "r") as firstfile, open(directory_input2, "w") as secondfile:
   
#    for line in firstfile :  
#         donnee = firstfile.readline(30)
#         secondfile.writelines(donnee)
    
# #recopie ligne par ligne en donnant un identifiant et un mot  depasse aléatoire a chaque personne dans le fichier text.txt

# #-----------------------------------

#print ("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")


# -----------------------------------
import os
import sys


count_letters("string")