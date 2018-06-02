import card
import csv

def add_card(deck, card):
	with open("./decks/"+ str(deck) + ".csv", "w+") as f:
		f.write(card.csv() + "\n")

		
