import random
import time

def createDecks():
    cards = []
    Suits = ['Clubs', 'Diamonds',
            'Hearts', 'Spades']
    Ranks = ['A', '2', '3', '4',
            '5', '6', '7', '8',
            '9', '10', 'J', 'Q', 'K']
    for i in range(8):
        for rank in Ranks:
            for suit in Suits:
                cards.append([rank,suit])
    return cards

def play():
    bustDealer = 0
    bustPlayer = 0
    dealtPlayer = []
    dealtDealer = []
    cards = createDecks()
    for i in range(4):
        dealt = random.choice(cards)
        if i < 2:
            dealtPlayer.append(dealt)
        else:
            dealtDealer.append(dealt)
        cards.remove(dealt)
    sum = sumOfCards(dealtPlayer)
    while sum < 17:
        dealt = random.choice(cards)
        dealtPlayer.append(dealt)
        sum = sumOfCards(dealtPlayer)
        if sum > 21:
            bustPlayer = 1
    sum = sumOfCards(dealtDealer)
    while sum < 17:
        dealt = random.choice(cards)
        dealtDealer.append(dealt)
        sum = sumOfCards(dealtDealer)
        if sum > 21:
            bustDealer = 1
    wins = win(dealtDealer, dealtPlayer, bustDealer, bustPlayer)
    return wins

def win(dealtDealer, dealtPlayer, bustDealer, bustPlayer):
    sumDealer = sumOfCards(dealtDealer)
    sumPlayer = sumOfCards(dealtPlayer)
    if (bustDealer == 1 and bustPlayer == 0) or (sumPlayer > sumDealer and bustPlayer == 0 and len(dealtDealer) < 5) or (len(dealtPlayer) >= 5 and bustPlayer == 0 and len(dealtDealer) < 5):
        wins = True
    elif (bustDealer == 1 and bustPlayer == 1) or sumDealer >= sumPlayer or (bustPlayer == 1 and bustDealer == 0) or len(dealtDealer) >= 5:
        wins = False
    return wins

def sumOfCards(dealtList):
    sum = 0
    ace = 0
    values = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
    for row in dealtList:
        if str(row[0]) == "A":
            ace = ace + 1
        else:
            sum = sum + values[row[0]]
    for i in range(ace):
        if (sum+11) <= 21:
            sum = sum + 11
        else:
            sum = sum + 1
    return sum

def displayCards(dealtDealer, dealtPlayer):
    print("Dealers Cards:")
    for row in dealtDealer:
        strDealer = str(row[0])+" of "+str(row[1])
        print(strDealer)
    print("Players Cards:")
    for row in dealtPlayer:
        strPlayer = str(row[0])+" of "+str(row[1])
        print(strPlayer)

def main():
    winsTotal = 0
    repeat = 100000
    for i in range(repeat):
        wins = play()
        if wins is True:
            winsTotal = winsTotal + 1
    print("The player and house will both stick once they equal or are over 17."
          "\nIn",repeat,"games against the house:"
                      "\nPlayer won",str(round((winsTotal/repeat)*100))+"% of the time.")

main()
