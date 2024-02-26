import random
Noms=[]
#Première partie du programme, l'entré des noms
nb=int(input("Nombres de personnes : "))
for x in range(0,nb):
    print("Personne",x+1,":")
    nom=str(input("Nom de la personnes : "))
    Noms.append(nom)
print(Noms)



random.shuffle(Noms)                #La fonction random.shuffle(x) permet de mélanger de manière aléatoire une liste
print(Noms)



"""
#Deuxième partie du programme, classement aléatoire des noms
index=[]
ordrefin=[]
for i in range(1,nb+1):
    print(i,"vérif 1")
    sel=random.randint(1,nb)
    if sel in index:
        sel=random.randint
    index.append(sel)
    print(sel,"vérif 2")
    nb=nb-1
"""


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