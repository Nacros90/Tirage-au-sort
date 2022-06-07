import random
Tirage=[]
nb=int(input("nombres de personnes : "))
for x in range(0,nb):
    nom=str(input("Nom de la personnes n°",x,": "))
    Tirage.append(nom)
for k in range(0,nb):
    select=random.randint(1,nb)
    Tirage[select]
    del Tirage[select]
    nb=nb-1