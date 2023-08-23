import random
import time

def createDecks():
    cards = []
    Suits = ['Clubs', 'Diamonds',
            'Hearts', 'Spades']
    Ranks = ['A', '2', '3', '4',
            '5', '6', '7', '8',
            '9', '10', 'J', 'Q', 'K']
    for rank in Ranks:
        for suit in Suits:
            cards.append([rank,suit])
    return cards

def dealCards(cards,player,balance):
    bet = 0
    playerCards = []
    for i in range(5):
        deal = random.choice(cards)
        playerCards.append(deal)
        cards.remove(deal)
    print(player,"Cards:")
    for card in playerCards:
        print(card[0],"of",card[1])
    print("\n")
    time.sleep(0.2)
    if player == "Player":
        bet = getBet(balance)
        if bet != 0:
            newHand(cards,playerCards)
    scoreRank = score(playerCards)
    return scoreRank, cards, bet

def getBet(balance):
    while True:
        bet = input("You have £"+str(round(balance,2))+". How much would you like to bet, with a minimum of £5? (Type 0 to exit) \n")
        try:
            bet = round(float(bet),2)
        except ValueError:
            print("Please enter numbers only.\n")
            continue
        if bet == 0:
            break
        elif bet <= balance and bet >= 5:
            break
        else:
            print("You can not bet that amount.\n")
            continue
    time.sleep(0.2)
    return bet

def newHand(cards,playerCards):
    listReshuffle = []
    cardsToRemove = []
    while True:
        newCards = input("How many cards would you like to reshuffle? (0-5) \n")
        try:
            newCards = int(newCards)
        except ValueError:
            print("Please enter a number.\n")
            continue
        if newCards > -1 and newCards < 6:
            break
        else:
            print("Please enter a number in range.\n")
    if newCards != 0:
        for i in range(newCards):
            time.sleep(0.2)
            while True:
                numReshuffle = input("Select a card to be reshuffled. (1-5) \n")
                try:
                    numReshuffle = int(numReshuffle)
                except ValueError:
                    print("Please enter a number.")
                    continue
                if (numReshuffle-1) in listReshuffle or numReshuffle < 1 or numReshuffle > 5:
                    print("Please enter a number in range and not already chosen.\n")
                    continue
                else:
                    break
            listReshuffle.append(numReshuffle-1)
        for num in listReshuffle:
            cardsToRemove.append(playerCards[num])
            deal = random.choice(cards)
            playerCards.append(deal)
            cards.remove(deal)
        for card in cardsToRemove:
            playerCards.remove(card)
        print("\n")
        time.sleep(0.2)
        print("Player Cards:")
        for card in playerCards:
            print(card[0],"of",card[1])
        print("\n")
        time.sleep(0.2)
            
def score(playerCards):
    Scores = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,
              'J':11,'Q':12,'K':13,'A':1}
    invScores = {v: k for k, v in Scores.items()}
    invScores[14]='A'
    cards = playerCards
    unscoredValues = []
    values = []
    suits = []
    scoreRank = []
    straight = False
    flush = False
    fullhouse = False
    twoPair = False
    for card in cards:
        unscoredValues.append(card[0])
        suits.append(card[1])
    for value in unscoredValues:
        values.append(Scores[value])
    values.sort()
    if (values[0]+1)==values[1] and (values[1]+1)==values[2] and (values[2]+1)==values[3] and (values[3]+1)==values[4]:
        straight = True
        straightHigh = value[4]
    if suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]:
        flush = True 
    for i in range(len(values)):
        if values[i] == 1:
            values[i] = 14
    values.sort()
    highCount = [0,0]
    for value in values:
        count = values.count(value)
        if count > highCount[0]:
            highCount = [count,value]        
    if highCount[0] == 3:
        for i in range(3):
            values.remove(highCount[1])
        if values[0] == values[1]:
            fullhouse = True
        for i in range(3):
            values.append(highCount[1])
        values.sort()
    if highCount[0] == 2:
        for i in range(2):
            values.remove(highCount[1])
        if values[0] == values[1] or values[0] == values[2] or values[1] == values[2]:
            twoPair = True
        for i in range(2):
            values.append(highCount[1])
        values.sort()
    if values == ['10','11','12','13','14'] and flush is True:
        scoreRank = [10,0,"a royal flush"]
    elif straight is True and flush is True:
        scoreRank = [9,straightHigh,"a straight flush"]
    elif highCount[0] == 4:
        scoreRank = [8,highCount[1],"four of a kind"]
    elif fullhouse is True:
        scoreRank = [7,highCount[1],"a full house"]
    elif flush is True:
        scoreRank = [6,values[4],"a flush"]
    elif straight is True:
        scoreRank = [5,straightHigh,"a straight"]
    elif highCount[0] == 3:
        scoreRank = [4,highCount[1],"three of a kind"]
    elif twoPair is True:
        scoreRank = [3,highCount[1],"two pairs"]
    elif highCount[0] == 2:
        scoreRank = [2,highCount[1],"a pair of "+str(invScores[highCount[1]])+"s"]
    else:
        scoreRank = [1,values[4],str(invScores[values[4]])+" high card"]
    return scoreRank

def winner(bot, player):
    print("Player had",player[2]+".",
          "\nComputer had",bot[2]+".")
    print("\n")
    time.sleep(0.2)
    if player[0] > bot[0] or (player[0] == bot[0] and player[1] > bot[1]):
        print("Player wins!")
        win = 1
    elif player == bot:
        print("Draw!")
        win = 0
    else:
        print("Player Loses!")
        win = -1
    print("\n")
    time.sleep(0.2)
    return win

def main():
    with open("balance.txt") as f:
        contents = f.readlines()
    balance = float(contents[0])
    cards = createDecks()
    player, cards, bet = dealCards(cards,"Player",balance)
    if bet != 0:
        bot, cards, cbet = dealCards(cards,"Computer",balance)
        win = winner(bot,player)
        if win == 1:
            balance = balance + bet
        if win == -1:
            balance = balance - bet
    print("Thanks for playing!"     
          "\nTotal balance remaining: £"+str(round(balance,2)))
    with open("balance.txt", "w") as f:
        f.write(str(balance))

main()
end=input("")
