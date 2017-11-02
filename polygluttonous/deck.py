import card
import csv

class Deck:
	
	def init(self, name, cards):
		self.name = name
		self.cards = []
		for card in cards:
			self.cards.append(card)
	
	def read(self, name):
		self.cards = []
		with open('%s.csv' % name, 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				card = card.create_card_from_csv(row)
