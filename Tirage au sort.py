import random
Tirage=[]
nb=int(input("Nombres de personnes : "))
for x in range(0,nb):
    print("Personne",x+1,":")
    nom=str(input("Nom de la personnes : "))
    Tirage.append(nom)
print(Tirage)
print("L'ordre des personnes est :")
for k in range(1,nb+1):
    print(k)
    select=random.randint(1,nb)
    print(select)
    nb=nb-1
    print(Tirage[select+1])
    del Tirage[select]                                              #Il y a un problème pour le nombre de tirage, une sortie de "range" est indiqué