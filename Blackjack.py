import random
import time

def createDecks():
    cards = []
    Suits = ['Clubs', 'Diamonds',
            'Hearts', 'Spades']
    Ranks = ['A', '2', '3', '4',
            '5', '6', '7', '8',
            '9', '10', 'J', 'Q', 'K']
#Create 8 decks as all used in Blackjack.
    for i in range(8):
        for rank in Ranks:
            for suit in Suits:
                cards.append([rank,suit])
    return cards

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
    return bet

def play(balance):
    while round(balance, 2) > 0:
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
        displayCards(dealtDealer, dealtPlayer)
        print("\n")
        time.sleep(0.5)
        bet = getBet(balance)
        if bet == 0:
            break
        sum = sumOfCards(dealtPlayer)
        while sum <= 21:
            hit = hitOrStick(sum)
            if hit is True:
                dealt = random.choice(cards)
                dealtPlayer.append(dealt)
                displayCards(dealtDealer,dealtPlayer)
                print("\n")
                time.sleep(0.5)
            elif hit is False:
                break
            sum = sumOfCards(dealtPlayer)
            if sum > 21:
                print("Player Bust")
                print("\n")
                time.sleep(0.5)
                bustPlayer = 1
        sum = sumOfCards(dealtDealer)
        while sum <= 17:
            dealt = random.choice(cards)
            dealtDealer.append(dealt)
            displayCards(dealtDealer, dealtPlayer)
            time.sleep(2)
            print("\n")
            sum = sumOfCards(dealtDealer)
            if sum > 21:
                print("Dealer Bust")
                print("\n")
                time.sleep(0.5)
                bustDealer = 1
        balance = win(dealtDealer, dealtPlayer, bustDealer, bustPlayer, balance, bet)
    return balance

def win(dealtDealer, dealtPlayer, bustDealer, bustPlayer, balance, bet):
    sumDealer = sumOfCards(dealtDealer)
    sumPlayer = sumOfCards(dealtPlayer)
    if (bustDealer == 1 and bustPlayer == 0) or (sumPlayer > sumDealer and bustPlayer == 0) or (len(dealtPlayer) >= 5 and bustPlayer == 0 and len(dealtDealer) < 5):
        print("You win!\n")
        time.sleep(0.5)
        balance = balance + bet
    elif (bustDealer == 1 and bustPlayer == 1) or sumDealer >= sumPlayer or (bustPlayer == 1 and bustDealer == 0) or len(dealtDealer) >= 5:
        print("You lose!\n")
        time.sleep(0.5)
        balance = balance - bet
    with open("balance.txt", "w") as f:
        f.write(str(balance))
    return balance

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

def hitOrStick(sum):
    while True:
        hit = input("Hit or Stick? \n")
        time.sleep(0.5)
        if hit.lower() == "hit":
            hit = True
            break
        elif hit.lower() == "stick" and sum > 15:
            hit = False
            break
        elif hit.lower() == "stick" and sum < 16:
            print("Can not stick under 16.\n")
            continue
        else:
            print("Invalid input.\n")
            continue
    return hit

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
    with open("balance.txt") as f:
        contents = f.readlines()
    balance = float(contents[0])
    balance = play(balance)
    print("Thanks for playing!"
          "\nTotal balance remaining: £"+str(round(balance,2)))
    with open("balance.txt", "w") as f:
        f.write(str(balance))

main()