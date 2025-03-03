import random
print ('Bienvenue dans le jeu : Pierre,papier,ciseaux')

choix = ["pierre","papier","ciseaux"]

score1=0
score2=0

for _ in range (3):
	user = input('pierre, papier , ciseaux ? ')
	bot= random.choice(choix)
	assert user in choix , 'faites un choix correcte '
	if user == bot :
		print("la partie est nulle ")
		print(f"vous avez joué :{user} et bot a joué {bot}")
	elif user == "pierre":
		if bot =="ciseaux":
			print(f"vous avez joué :{user} et bot a joué {bot}")
			print(" Vous remportz le point")
			score1+=1
		else : 
			print(f"vous avez joué :{user} et bot a joué {bot}")
			print("Bot remporte le point")
			score2+=1
	elif user =="papier":
		if bot == "pierre":
			print(f"vous avez joué :{user} et bot a joué {bot}")
			print ("Vous remportez le point")
			score1+=1
		else :
			print(f"vous avez joué :{user} et bot a joué {bot}")
			print("Bot remporte le point")
			score2+=1
	elif user == "ciseaux":
		if bot == "papier":
			print(f"vous avez joué :{user} et bot a joué {bot}")
			print("Vous remportez le point")
			score1+=1
		else :
			print(f"vous avez joué :{user} et bot a joué {bot}") 
			print ("Bot remporte le point")
			score2+=1
	print("**********************************************")
	print (f"vous avez: {score1} et bot en a: {score2}")
			
if score1 < score2:
	print (f"vous avez: {score1} et bot en a: {score2}")
	print ("Vous avez perdu :( !" )		
else : 
	print (f"vous avez: {score1} et bot en a: {score2}")
	print("Vous avez gagné :) ! ")	
			



