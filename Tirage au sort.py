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
    sel=random.randint(1,nb)
    while sel in index:
        sel=random.randint(1,nb)
    index.append(sel)
    ordrefin.append(Noms[sel-1])
print("Le nouvel ordre des noms est :",ordrefin)