import random
# Choisir un nombre aléatoire compris entre 1 et 100
number_to_guess = random.randint(1, 100)
# Initialiser le nombre de tentatives à 0
tries = 0
# Boucle jusqu'à ce que le nombre soit deviné
while True:
  # Demander à l'utilisateur de saisir un nombre
  guess = int(input("Devinez un nombre entre 1 et 100 : "))
  tries += 1
  # Vérifier si le nombre deviné est plus grand, plus petit ou égal au nombre à trouver
  if guess < number_to_guess:
    print("Le nombre à deviner est plus grand.")
  elif guess > number_to_guess:
    print("Le nombre à deviner est plus petit.")
  else:
    # Si le nombre est deviné, afficher le nombre de tentatives
    print("Félicitations! Vous avez deviné le nombre en", tries, "tentatives.")
    break