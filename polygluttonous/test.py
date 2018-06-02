import card
import card_operations

c = card.Card(1, 'front', 'back') #creates card with id 1, front, back, and creation time t
card_operations.add_card( "my_deck", c)

print vars(c)

c.guess()
