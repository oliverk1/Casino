import random

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
    ifNum = choice.isdigit()
    if (colour == "black" and choice == "black") or (colour == "red" and choice == "red") or (colour == "odd" and choice == "odd") or (colour == "even" and choice == "even"):
        win = bet
    elif colour == "green" and choice == "green":
        win = bet * 35
    elif ifNum is True:
        if int(spin) == int(choice):
            win = bet *35
    return win

def main():
    total1 = 0
    total35 = 0
    loss = 0
    win1to1 = []
    win35to1 = []
    bet = 5
    repeat = 1000000
    for i in range(repeat):
        spin, colour = rouletteSpin()
        win1to1.append(getWinnings(spin, colour, "red", bet))
        win35to1.append(getWinnings(spin, colour, "7", bet))
    for row in win1to1:
        total1 = total1 + row
        if row > 0:
            loss = loss + row
    for row in win35to1:
        total35 = total35 + row
        if row > 0:
            loss = loss + row
    totalProfit = ((repeat*bet)*2) - loss
    total1 = total1 / repeat
    total35 = total35 / repeat
    print("Out of",repeat,"spins:"
            "\nProfit is",str(round((totalProfit/(repeat*2*bet)*100),2))+"%"
            "\nThe average return on £5 per bet 1 to 1 bets is",round(total1,2),"pounds."
            "\nThe average return on £5 per bet on 35 to 1 bets is",round(total35,2),"pounds.")

main()
