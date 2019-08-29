noms = ['Hamza' , 'Othman' , 'Soueiman']
adjs = ['Sgue3' , 'Tigog' , 'Nze9']

def combinateur_de_liste(noms, adjs) -> list:
    liste_finale1 = []
    liste_finale2 = []
    for i in noms:
        for j in adjs:
            liste_finale1.append(i)
            liste_finale2.append(j)
    return list(zip(liste_finale1 , liste_finale2))
liste_finale = combinateur_de_liste(noms,adjs)
print(combinateur_de_liste(noms,adjs))