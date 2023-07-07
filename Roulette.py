import random

def getBet(balance):
    while True:
        bet = input("You have £"+str(round(balance,2))+". How much would you like to bet, with a minimum of £5? (Type 0 to exit) ")
        try:
            bet = round(float(bet),2)
        except ValueError:
            print("Please enter numbers only.")
            continue
        if bet == 0:
            break
        elif bet <= balance and bet >= 5:
            break
        else:
            print("You can not bet that amount.")
            continue
    return bet

def getChoice():
    while True:
        choice = input("What number/colour (0-36 or Red/Green/Black or Odd/Even) would you like to bet on? ")
        choice = choice.lower()
        ifNum = choice.isdigit()
        if ifNum is True:
            if 0 <= int(choice) <= 36:
                break
            else:
                print("Please enter a valid number/colour.")
                continue
        if choice == "red" or choice == "green" or choice == "black" or choice == "odd" or choice == "even":
            break
        else:
            print("Please enter a valid number/colour.")
            continue
    return choice

def rouletteSpin():
    spin = random.randint(0,36)
    if spin == 0:
        colour = "green"
    elif spin%2:
        colour = "red"
    else:
        colour = "black"
    return spin, colour

def getWinnings(spin, colour, choice, bet):
    win = -bet
    print(spin, colour)
    ifNum = choice.isdigit()
    if (colour == "black" and choice == "black") or (colour == "red" and choice == "red") or (colour == "odd" and choice == "odd") or (colour == "even" and choice == "even"):
        win = bet
        print("You win 1 to 1.")
    elif colour == "green" and choice == "green":
        win = bet * 35
        print("You win 35 to 1.")
    elif ifNum is True:
        if int(spin) == int(choice):
            win = bet *35
            print("You win 35 to 1.")
    return win

def main():
    with open("balance.txt") as f:
        contents = f.readlines()
    balance = float(contents[0])
    while round(balance, 2) > 0:
        print("Balance: £"+str(round(balance,2)))
        bet = getBet(balance)
        if bet == 0:
            break
        choice = getChoice()
        spin, colour = rouletteSpin()
        win = getWinnings(spin, colour, choice, bet)
        balance = balance + win
        with open("balance.txt", "w") as f:
            f.write(str(balance))
        print("\n")
    print("Thanks for playing!"
          "\nTotal balance remaining: £"+str(round(balance,2)))
    with open("balance.txt", "w") as f:
        f.write(str(balance))
main()
