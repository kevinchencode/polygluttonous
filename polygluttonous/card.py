import sys
import time
import random
from fuzzywuzzy import fuzz

#TODO: write code that exports activity logs
class Card:

	back_synonyms = []
	STACK_TIME = [5, 25, 120, 600, 3600, 3600*5, 3600*24, 3600*24*5, 3600*24*25, 3600*24*30*4, 3600*24*365*2] #returns value in seconds
	def __init__(self, ID, frontside, backside):
		
		#in this order: frontside, backside, 
		
		'''
		Cards are the fundamental building block of all spaced repitition software. You show the user the frontside, they guess the backside 
		then if they got it right, increase stack, otherwise, set stack back to zero.
		'''
		
		#fronside of the card
		self.frontside = frontside
		
		#backside of the card
		self.backside = backside
		
		'''
		a stack is the level of memory the card has built up so far. Stacks currently go from level 0 to level 10 where
		level 0 is things the user cannot remember, while level 5 is things the user has remembered after lots of spaced repitition.
		These are the time intervals for each level (chosen from Pimslur, to be changed in the future):
		0  ->  5 seconds
		1  ->  25 seconds
		2  ->  2 minutes
		3  ->  10 minutes
		4  ->  1 hour
		5  ->  5 hours
		6  ->  1 day
		7  ->  5 days
		8  ->  25 days
		9  ->  4 months
		10 ->  2 years
		'''
		self.stack = 0 
		
		'''
		this is the time when the card was added to the deck. Kept for logging/querying purposes
		'''	
		self.time_added = time.time()
		
		'''
		this is the time the card was last used
		'''
		self.time_last_used = None

		'''
		this is the calculated time for the future
		''' 
		self.time_next = self.time_added + 5.0

		'''
		this tells if a card is due to be reviewed, technecally superfluous, but keeps me from constantly rechecking time
		'''
		self.due = False

		self.ID = ID #generate_ID() as soon as I figure out how this is going to work

	#procedure if the card was answered correctly
	def correct(self):
		if self.stack != 10:
			self.stack += 1
		self.time_last_used = time.time()
		#next time adds a random number to randomize card order if cards are in same stack and accessed in same session
		self.time_next = self.time_last_used + Card.STACK_TIME[self.stack] \
		+ max(random.randint(0, 30), random.randint(0, Card.STACK_TIME[self.stack]))
	
		self.due = False
		return

	#procedure if the card was answered incorrectly
	def incorrect(self):
		self.stack = 0
		self.time_last_used = time.time()
		self.time_next = self.time_last_used + 5
		self.due = False
		return

	#procedure to return whether or not a card is ready to be shown
	def check_card_ready(self):
		if time.time() > self.time_next:
			return True
		return False

	#procedure to tell how much time if left before 
	def return_time_before_ready(self):
		time_diff = self.time_next - time.time()
		return time_diff

	#basic printing ability for object
	def __str__(self):
		at = vars(self)
		return ', '.join("{%s: %s}" % item for item in at.items())
	#saving items as a csv file
	def csv(self):
		return ', '.join("%s" % value for item, value in vars(self).items())

	#gives the front of the card, makes you guess the backside
	def guess(self):
		print self.frontside
		inp = raw_input()
		match = fuzz.ratio(inp, self.backside)
		print match
		if match > 70:
			self.correct()
			return True
		else:
			for syn in self.back_synonyms:
				fuzz.ratio(inp, syn)
				if match > 70:
					self.correct()
					return true
			self.incorrect()
			return False
	#given a tuple, create the card for it
	
	def add_back_synonym(synonym):
		self.back_synonyms = self.back_synonyms + synonym
		return

	def import_row(self, row):
		self.frontside,	self.backside,	self.stack,	self.time_added,	self.time_last_used, \
		self.time_next,	self.due,	self.ID 	= row
		return	
	
