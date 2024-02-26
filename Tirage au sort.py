import random
Noms=[]
#Première partie du programme, l'entré des noms
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
    print(i,"vérif 1")
    sel=random.randint(1,nb)
    while sel in index:
        sel=random.randint(1,nb)
    index.append(sel)
    print(sel,"vérif 2")
    ordrefin.append(Noms[sel-1])
print("Le nouvel ordre des noms est :",ordrefin)



"""
                #Ancienne version qui présente trop de pb
print("L'ordre des personnes est :")
for k in range(1,nb+1):
    print(k)
    select=random.randint(1,nb)
    print(select)
    nb=nb-1
    print(Noms[select+1])
    del Noms[select]                          #Il y a un problème pour le nombre de tirage, une sortie de "range" est indiqué
"""