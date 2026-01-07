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
    compteur += 1  


# test 3
for i in range(5):
    print(f"Indice : {i}")


# test 4
while True:
    reponse = input("Tapez 'quitter' pour sortir : ")
    if reponse == "quitter":
        print("Sortie de la boucle...")
        break    