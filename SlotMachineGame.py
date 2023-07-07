#Random used to get random symbols from the slot machine.
import random

def spinChoice():
#While True used to ensure correct formatted input.
    while True:
        spinChoice = input("SPIN? (Y/N) ")
#.lower() used so every possible combination doesn't have to be searched for.
        spinChoice = spinChoice.lower()
        if spinChoice == "y":
            spin = True
            break
        elif spinChoice == "n":
            spin = False
            break
        else:
            continue
    return spin

def play(balance):
#The slot machine consists of three reels each with ten symbols.
    reel = ["Lemon","Cherry","Grape","Orange","Melon","Seven","Ace","Bell","Crown","Jackpot"]
#A dictionary is used to find the amount won per spin.
    win = {"Lemon":0.25,"Cherry":0.5,"Grape":0.75,"Orange":1,"Melon":1,"Seven":1,"Bell":1,"Ace":5,"Crown":10,"Jackpot":250}
    reelSpun = []
    reelStr = ""
#Three symbols are randomly found.
    for i in range(3):
        reelItem = random.choice(reel)
        reelSpun.append(reelItem)
        reelStr = reelStr + reelItem + " "
#Prints to the player what has been spun.
    print(reelStr)
    result = all(item == reelSpun[0] for item in reelSpun)
#If three match then the player wins and the dictionary is used to see how much is won.
    if (result):
        print("You won!")
# Their winnings is appended to their balance.
        balance = balance + win[reelItem]
    return balance



def main():
# Access a txt file with the balance so it can be used amongst casino games.
# Gets balance from txt file and converts the string to float.
    with open("balance.txt") as f:
        contents = f.readlines()
    balance = float(contents[0])
#Loop as long as player has money and wished to spin again.
    spin = True
    while balance > 0.5 and spin is True:
        print("Balance: £"+str(round(balance,2)),
              "\nSpins Left:",int(balance//0.5))
#Finds if the user wants to spin the wheel.
        spin = spinChoice()
        if spin is True:
#The slot machine is spun and their balance if they win is returned.
            balance = balance - 0.5
            balance = play(balance)
            with open("balance.txt", "w") as f:
                f.write(str(balance))
    print("Thanks for playing!"
          "\nTotal balance remaining: £"+str(round(balance,2)))
#Rewrite new balance
    with open("balance.txt", "w") as f:
        f.write(str(balance))

main()
