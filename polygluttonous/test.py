import card

t  = time.time()
c = card.Card(1, 'front', 'back') #creates card with id 1, front, back, and creation time t

print vars(c)

c.guess()
