
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

# import os
# import sys

# def count_letters(string):
#   upper_count = 0
#   lower_count = 0
#   string = sys.argv[1]
#   for char in string:
#     if char.isupper():
#       upper_count += 1
#     elif char.islower():
#       lower_count += 1
#   return print(f"Nombre de Majuscule : {upper_count}     Nombre de Minuscule : {lower_count}")

# count_letters("string")


# -----------------------------------

# nombre = float(input("Saisir un nombre"))

# if nombre > 0 :
#         print ("Positif")
# elif nombre < 0 :
#         print ("Negatif")
# elif nombre == 0 :
#         print ("Neutre")


# -----------------------------------
# phrase = input('Ta phrase :')

# a = []

# a.extend(phrase.split())

# print(a)


# -----------------------------------
# lettre = input ("Entrez une lettre")

# voyelles = ["a","e","i","o","u","y"]

# consonnes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]



# if lettre in consonnes:

#    print("C'est une consonne")

# else:

#    print("C'est une voyelle")

# -----------------------------------

# liste_nbr = [1,2,10,100]
# print (max(liste_nbr))

# -----------------------------------

# import argparse

# parser = argparse.ArgumentParser(
#                     prog = 'Mon programme qui écrit un emoji',
#                     description = 'Ecrit des emojis',
#                     )

# parser.add_argument('emoji')           # positional argument
# parser.add_argument('-n', '--number',type=int, choices=range(3, 16), default=5)      # option that takes a value

# args = parser.parse_args()
# # print(args.emoji, args.number)

# for i in range(args.number):
#     print(args.emoji, end="")

# -----------------------------------
# import sys
# import os


# if len(sys.argv) < 4:
#     print("Merci d'indiquer le nom du fichier, la chaine de caractere a remplacer et la chaine de caractere de remplacement.")
#     sys.exit()
    
# filename = sys.argv[1]
# string = sys.argv[2]
# replace_string = sys.argv[3]

# if not os.path.exists(filename):
#     print("Le fichier n'existe pas.")
#     sys.exit()

# with open(filename, "r") as file:
#     content = file.read()

# new_content = content.replace(string, replace_string)

# with open(filename, "w") as file:
#     file.write(new_content)
# -----------------------------------

# import paramiko 

# ssh = paramiko.SSHClient()

# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh.connect('192.168.1.30', username ='francois' , key_filename="C:\\Users\\ROCHE François\\.ssh\\id_rsa")

# stdin, stdout, stderr = ssh.exec_command('timedatectl')

# print(stdout.readlines())

# ssh.close()
# -----------------------------------
import paramiko

srv = pysftp.Connection(host="192.168.1.30", username="francois",
password="password")

with srv.cd("/home/francois/Documents"):
        srv.put("C:\Users\ROCHE François\Desktop\testsftp.txt")

srv.close()