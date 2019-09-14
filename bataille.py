import random
import sys
player_1_name = str(input("Le nom du premier joueur: "))
player_2_name = str(input("Le nom du deuxième joueur: "))

cards = []
for i in range(4):
	for y in range(10):
		cards.append((y))

cards_player_1 = []
cards_player_2 = []

for i in range(20):
	y = random.choice(cards)
	cards_player_1.append(y)
	cards.remove(y)

cards_player_2 = cards

print("player 1 cards: ",cards_player_1)
print("player 2 cards: ",cards_player_2)

def game():
	player_1_points = []
	player_2_points = []
	for i in range(20):
		if cards_player_1[i] < cards_player_2[i]:
			print(i, "because" ,"(1) ", cards_player_1[i], "<",  cards_player_2[i], "(2) ","player_2 gets 1 point")
			player_2_points.append(1)

		elif cards_player_1[i] > cards_player_2[i]:
			print(i, "because" ,"(1) ", cards_player_1[i], ">", cards_player_2[i], "(2) ","player_1 gets 1 point")
			player_1_points.append(1)		

	
		
		elif cards_player_1[i] == cards_player_2[i]:
			print(i ," equality")
			continue
				
		elif cards_player_1[i] == cards_player_2[i]:
			print(i, " equality")
			continue

	if len(player_1_points) < len(player_2_points):
		winner = "The winner is " + player_2_name
	elif len(player_1_points) > len(player_2_points):
		winner = "The winner is " + player_1_name
	else:
		winner = "The winner is No one has won !!!"
	return winner

print(game())
