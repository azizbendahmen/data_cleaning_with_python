donnees_brutes = [
    "Jean, 45, Paris, ACTIF",
    "Marie, 32, Lyon, INACTIF",
    "Pierre, 28, Marseille, ACTIF",
    "Sophie,  , Bordeaux, ACTIF" # Note l'âge manquant
]

final_liste =[]

for donne in donnees_brutes:
    print(donne)
    don=donne.split(",")
    don = [d.strip() for d in don]
    
    nom = don[0]
    age = don[1]
    ville = don[2]
    statut = don[3]
    
    if age =="":
        age = "Âge manquant"
    else : 
        age=int(age)
        
    utilisateur = {
        "nom": nom,
        "age": age,
        "ville": ville,
        "statut": statut
    }
    final_liste.append(utilisateur)
print(final_liste)
