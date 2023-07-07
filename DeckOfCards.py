cards = []
Suits = ['Club', 'Diamond',
         'Heart', 'Spade']
Ranks = ['A', '2', '3', '4',
         '5', '6', '7', '8',
         '9', '10', 'J', 'Q', 'K']
for rank in Ranks:
    for suit in Suits:
        cards.append([rank,suit])
print(cards)
