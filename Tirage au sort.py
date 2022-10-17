import random
Tirage=[]
nb=int(input("nombres de personnes : "))
for x in range(0,nb):
    nom=str(input("Nom de la personnes: "))
    Tirage.append(nom)
"""print(Tirage)"""
print("l'ordre des personnes est :")
for k in range(1,nb):
    select=random.randint(1,nb)
    nb=nb-1
    print(Tirage[select])
    del Tirage[select]                                              #Il y a un problème pour le nombre de tirage, une sortie de "range" est indiqué