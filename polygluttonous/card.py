import sys
import time

class Card:
	
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
		self.time_next = time.time() + 5.0

		'''
		this tells if a card is due to be reviewed, technecally superfluous, but keeps me from constantly rechecking time
		'''
		self.due = False
	
		'''
		
		'''


