import random
Tirage=[]
nb=int(input("nombres de personnes : "))
for x in range(0,nb):
    nom=str(input("Nom de la personnes: "))
    Tirage.append(nom)
for k in range(0,nb):
    select=random.randint(1,nb)
    Tirage[select]                                                  #problème à la ligne 9 je pense que c'est
    nb=nb-1                                                         #l'assignation de la string dans la liste
print("L'ordre des personnes est",Tirage,".")