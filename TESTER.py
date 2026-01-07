# test 1
note = 12
seuil = 10

if note >= seuil:
    print("L'étudiant est admis.")
else:
    print("L'étudiant est refusé.")


# test 2
compteur = 1
while compteur <= 5:
    print(f"Tour numéro {compteur}")
    compteur += 1  # Très important pour ne pas rester bloqué à l'infini !


# test 3
# Affiche les nombres de 0 à 4
for i in range(5):
    print(f"Indice : {i}")


# test 4
while True:
    reponse = input("Tapez 'quitter' pour sortir : ")
    if reponse == "quitter":
        print("Sortie de la boucle...")
        break    