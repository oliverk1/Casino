import random

def spinChoice():
    while True:
        spinChoice = input("SPIN? (Y/N) ")
        if spinChoice == "Y" or spinChoice == "y":
            continuePlay = True
            spin = True
            break
        elif spinChoice == "N" or spinChoice == "n":
            continuePlay = False
            spin = False
            break
        else:
            continue
    return continuePlay, spin

def play(balance):
    reel = ["Lemon","Cherry","Grape","Orange","Melon","Seven","Ace","Bell","Crown","Jackpot"]
    win = {"Lemon":0.25,"Cherry":0.5,"Grape":0.75,"Orange":1,"Melon":1,"Seven":1,"Bell":1,"Ace":5,"Crown":10,"Jackpot":250}
    reelSpun = []
    reelStr = ""
    for i in range(3):
        reelItem = random.choice(reel)
        reelSpun.append(reelItem)
        reelStr = reelStr + reelItem + " "
    print(reelStr)
    result = all(item == reelSpun[0] for item in reelSpun)
    if (result):
        print("You won!")
        balance = balance + win[reelItem]
    return balance



def main():
    balance = "£10.74"
    balance = float(balance.lstrip("£"))
    continuePlay = True
    while balance > 0.5 and continuePlay is True:
        print("Balance: £"+str(round(balance,2)),
              "\nSpins Left:",int(balance//0.5))
        continuePlay, spin = spinChoice()
        if spin is True:
            balance = play(balance)
            balance = balance - 0.5
    print("Thanks for playing!"
          "\nTotal balance remaining: £"+str(round(balance,2)))

main()