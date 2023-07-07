#Random used to "Spin" the roulette wheel.
import random

def getBet(balance):
# While True is used to ensure a correct input is used.
    while True:
        bet = input("You have £"+str(round(balance,2))+". How much would you like to bet, with a minimum of £5? (Type 0 to exit) ")
# The input is tried as a float to ensure it is in correct format.
        try:
            bet = round(float(bet),2)
# except ValueError ensures that an error doesn't break the code.
        except ValueError:
            print("Please enter numbers only.")
            continue
        if bet == 0:
            break
# Bet must be greater than the minimum and equal to or less than their balance.
        elif bet <= balance and bet >= 5:
            break
        else:
            print("You can not bet that amount.")
            continue
    return bet

def getChoice():
#While True used to ensure correct formatted input
    while True:
        choice = input("What number/colour (0-36 or Red/Green/Black or Odd/Even) would you like to bet on? ")
        choice = choice.lower()
#checks if player wants to bet on a number.
        ifNum = choice.isdigit()
#If they bet on a number it must be in range.
        if ifNum is True:
            if 0 <= int(choice) <= 36:
                break
            else:
                print("Please enter a valid number/colour.")
                continue
#If they bet on a colour it must be a correct colour.
        if choice == "red" or choice == "green" or choice == "black" or choice == "odd" or choice == "even":
            break
        else:
            print("Please enter a valid number/colour.")
            continue
    return choice

def rouletteSpin():
#Random number is spun between 0-36.
    spin = random.randint(0,36)
#The number is assigned to its relevant colour.
    if spin == 0:
        colour = "green"
    elif spin%2:
        colour = "red"
    else:
        colour = "black"
    return spin, colour

def getWinnings(spin, colour, choice, bet):
#The win is initially minus their bet.
    win = -bet
    print(spin, colour)
    ifNum = choice.isdigit()
#If they win on a 1 to 1 bet they win their bet.
    if (colour == "black" and choice == "black") or (colour == "red" and choice == "red") or (colour == "odd" and choice == "odd") or (colour == "even" and choice == "even"):
        win = bet
        print("You win 1 to 1.")
#If they win a 35 to 1 bet they win 35 times their bet.
    elif colour == "green" and choice == "green":
        win = bet * 35
        print("You win 35 to 1.")
    elif ifNum is True:
        if int(spin) == int(choice):
            win = bet *35
            print("You win 35 to 1.")
    return win

def main():
# Access a txt file with the balance so it can be used amongst casino games.
# Gets balance from txt file and converts the string to float.
    with open("balance.txt") as f:
        contents = f.readlines()
    balance = float(contents[0])
#As long as the player has money and doesn't choose to exit the game continues.
    while round(balance, 2) > 0:
        print("Balance: £"+str(round(balance,2)))
#The bet is got from the player.
        bet = getBet(balance)
        if bet == 0:
            break
#The choice from the roulette wheel is got from the player.
        choice = getChoice()
#The roulette is spin and a random number and colour from the wheel is returned.
        spin, colour = rouletteSpin()
#Checks if player has won and how much.
        win = getWinnings(spin, colour, choice, bet)
#Their balance gets what they won appended. (Can be minus their bet if they didn't win.)
        balance = balance + win
        with open("balance.txt", "w") as f:
            f.write(str(balance))
        print("\n")
    print("Thanks for playing!"
          "\nTotal balance remaining: £"+str(round(balance,2)))
#Rewrite new balance
    with open("balance.txt", "w") as f:
        f.write(str(balance))
main()
end = input("")