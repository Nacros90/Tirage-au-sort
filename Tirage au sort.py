import random

#Première partie du programme, l'entré des noms
Noms=[]
nb=int(input("Nombres de personnes : "))
for x in range(0,nb):
    print("Personne",x+1,":")
    nom=str(input("Nom de la personnes : "))
    Noms.append(nom)
print("La liste des noms est :",Noms)

#Deuxième partie du programme, classement aléatoire des noms
index=[]
ordrefin=[]
for i in range(1,nb+1):
    sel=random.randint(1,nb)                            #séléction d'un index aléatoire
    while sel in index:
        sel=random.randint(1,nb)                        #permet d'éviter de choisir plusieur fois le même index
    index.append(sel)
    ordrefin.append(Noms[sel-1])                        #ajoute à la liste ordrefin l'élément de la liste Noms correspondant à l'index choisi
print("Le nouvel ordre des noms est :",ordrefin)