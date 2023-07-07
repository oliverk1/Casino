#Random needed to randomly deal cards from Blackjack deck.
import random
#Time needed so user is not overwhelmed with text.
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
#While True is used to ensure a correct input is used.
    while True:
        bet = input("You have £"+str(round(balance,2))+". How much would you like to bet, with a minimum of £5? (Type 0 to exit) \n")
#The input is tried as a float to ensure it is in correct format.
        try:
            bet = round(float(bet),2)
#except ValueError ensures that an error doesn't break the code.
        except ValueError:
            print("Please enter numbers only.\n")
            continue
        if bet == 0:
            break
#Bet must be greater than the minimum and equal to or less than their balance.
        elif bet <= balance and bet >= 5:
            break
        else:
            print("You can not bet that amount.\n")
            continue
    return bet

def play(balance):
#This runs as long as the player has balance and doesn't choose to exit
    while round(balance, 2) > 0:
        bustDealer = 0
        bustPlayer = 0
        dealtPlayer = []
        dealtDealer = []
#Create the 8 decks used in a Blackjack game.
        cards = createDecks()
#Deals the player and dealer two cards each.
#Cards are removed from the decks so Blackjack odds remain true to the original
        for i in range(4):
            dealt = random.choice(cards)
            if i < 2:
                dealtPlayer.append(dealt)
            else:
                dealtDealer.append(dealt)
            cards.remove(dealt)
#Player is shown the cards dealt to them and the dealer.
        displayCards(dealtDealer, dealtPlayer)
        print("\n")
        time.sleep(0.5)
#Get the players bet.
        bet = getBet(balance)
#If they choose no bet this exits the game.
        if bet == 0:
            break
#Whilst player is not bust the game continues unless they choose to stick.
        sum = sumOfCards(dealtPlayer)
        while sum <= 21:
#Get player's choice to stick or hit.
            hit = hitOrStick(sum)
#If they choose to hit a card is dealt and displayed.
            if hit is True:
                dealt = random.choice(cards)
                dealtPlayer.append(dealt)
                displayCards(dealtDealer,dealtPlayer)
                print("\n")
                time.sleep(0.5)
#If they stick it breaks the loop.
            elif hit is False:
                break
#Player can't be over 21 otherwise they are bust and lose.
            sum = sumOfCards(dealtPlayer)
            if sum > 21:
                print("Player Bust")
                print("\n")
                time.sleep(0.5)
                bustPlayer = 1
#Once the player is finished the dealer plays.
#The dealer must always stick once they are 17 or over.
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
#Win conditions are now checked to see who wins and balance is appended as relevant.
        balance = win(dealtDealer, dealtPlayer, bustDealer, bustPlayer, balance, bet)
    return balance

def win(dealtDealer, dealtPlayer, bustDealer, bustPlayer, balance, bet):
    sumDealer = sumOfCards(dealtDealer)
    sumPlayer = sumOfCards(dealtPlayer)
#The player is at a disadvantage and loses whenever they draw with the dealer.
    if (bustDealer == 1 and bustPlayer == 0) or (sumPlayer > sumDealer and bustPlayer == 0 and len(dealtDealer) < 5) or (len(dealtPlayer) >= 5 and bustPlayer == 0 and len(dealtDealer) < 5):
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
#Picture cards have specific values so a dictionary is used to ensure correct values are summed.
    values = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}
    for row in dealtList:
        if str(row[0]) == "A":
            ace = ace + 1
        else:
            sum = sum + values[row[0]]
#If an ace is present it can either be 1 or 11. If Ace being 11 would make the user bust it is changed to 1.
    for i in range(ace):
        if (sum+11) <= 21:
            sum = sum + 11
        else:
            sum = sum + 1
    return sum

def hitOrStick(sum):
#While True to ensure correct formatted input
    while True:
        hit = input("Hit or Stick? \n")
        time.sleep(0.5)
#.lower() is used so capitals are not relevant
        if hit.lower() == "hit":
            hit = True
            break
#Player can only stick if their total is 16 or over.
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
#Each card is printed in a user-friendly string format.
    for row in dealtDealer:
        strDealer = str(row[0])+" of "+str(row[1])
        print(strDealer)
    print("Players Cards:")
    for row in dealtPlayer:
        strPlayer = str(row[0])+" of "+str(row[1])
        print(strPlayer)

def main():
#Access a txt file with the balance so it can be used amongst casino games.
#Gets balance from txt file and converts the string to float.
    with open("balance.txt") as f:
        contents = f.readlines()
    balance = float(contents[0])
#Runs the play function to start the game and returns balance in order to rewrite the txt file.
    balance = play(balance)
    print("Thanks for playing!"
          "\nTotal balance remaining: £"+str(round(balance,2)))
#Rewrite new balance
    with open("balance.txt", "w") as f:
        f.write(str(balance))

main()