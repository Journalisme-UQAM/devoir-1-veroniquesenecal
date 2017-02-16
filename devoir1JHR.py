#coding : utf-8

for annee in range(30000,100000):
    print(annee)

for annee in range(0,10):
    print("0000{}".format(annee))
    
for annee in range(10,100):
    print("000{}".format(annee))

for annee in range(100,1000):
    print("00{}".format(annee))
    
for annee in range(1000,10000):
    print("0{}".format(annee))
    
for annee in range(10000,18000):
    print(annee)

#####

# Solution intéressante, mais il est possible de rédiger un script plus court.
# Voici l'une de mes propositions:

for a in range(1930,2018): # Boucle qui passe toutes les années de 1930 à 2017
	for x in range(1001,2000): # Boucle qui passe les 1000 numéros de permis possible à chaque année
	# J'imprime ensuite un assemblage fait de :
	# D'abord, je transforme les années en «string» (chaîne de caractères) et je n'en conserve que les deux derniers caractères
	# Puis je transforme aussi en «string» les nombres générés par la 2e boucle (qui va de 1000 à 1999) et je n'en conserve que les trois derniers caractères
		print(str(a)[2:] + str(x)[1:])


# Solution identique à celle de Maxime Hébert. Il y a apparence de plagiat. Je passe l'éponge pour cette fois, mais le devoir 2 que vous me rendrez, Maxime et toi, devra être différent.