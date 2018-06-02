import card
import csv

def add_card(deck, card):
	with open("./decks"+ str(deck), "r+"):
		
