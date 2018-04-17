import card
import csv

class Deck:
	
	def init(self, name, cards):
		self.name = name
		self.cards = []
		for card in cards:
			self.cards.append(card)
	
