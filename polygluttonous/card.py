import sys
import time

#TODO: write code that exports activity logs

class Card:
	STACK_TIME = [5, 25, 120, 600, 3600, 3600*5, 3600*24, 3600*24*5, 3600*24*25, 3600*24*30*4, 3600*24*365*2] #returns value in seconds
	def __init__(self, frontside, backside, time_added):
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

		self.ID = 0 #generate_ID() as soon as I figure out how this is going to work

	#procedure if the card was answered correctly
	def correct(self):
		if self.stack != 10:
			self.stack += 1
		self.time_last_used = time.time()
		self.time_next = self.time_last_used + Card.STACK_TIME[self.stack]
		self.due = False

	#procedure if the card was answered incorrectly
	def incorrect(self):
		self.stack = 0
		self.time_last_used = time.time()
		self.time_next = self.time_last_used + 5
		self.due = False

	#procedure to return whether or not a card is ready to be shown
	def check_card_ready(self):
		if time.time() > self.time_next:
			return True
		return False

	#procedure to tell how much time if left before 
	def return_time_before_ready(self):
		time_diff = self.time_next - time.time()
		return time_diff

	def __str__(self):
		return ', '.join("{%s: %s}" % item for item in at.items())
	
