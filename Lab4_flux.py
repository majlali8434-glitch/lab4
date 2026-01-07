seuil = 10
notes = []

while True:
    entree = input("Entrez une note (ou tapez 'stop' pour finir) : ").strip().lower()
    
    if entree == "stop":
        break  
        
    try:
        note = float(entree)
       
        notes.append(note)
    except ValueError:
        print("Erreur : Merci d'entrer un nombre valide.")

print("\n--- RÉSUMÉ DES RÉSULTATS ---")
for index, note in enumerate(notes, start=1):
    # d. Déterminer le statut (Admis ou Refusé)
    if note >= seuil:
        statut = "Admis"
    else:
        statut = "Refusé"
    
    print(f"Étudiant {index} : Note {note}/20 -> {statut}")