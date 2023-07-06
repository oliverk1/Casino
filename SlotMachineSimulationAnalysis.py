import random

def play(winTotal):
    reel = ["Lemon","Cherry","Grape","Orange","Melon","Seven","Ace","Bell","Crown","Jackpot"]
    win = {"Lemon":0.25,"Cherry":0.5,"Grape":0.75,"Orange":1,"Melon":1,"Seven":1,"Bell":1,"Ace":5,"Crown":10,"Jackpot":250}
    reelSpun = []
    reelStr = ""
    for i in range(3):
        reelItem = random.choice(reel)
        reelSpun.append(reelItem)
        reelStr = reelStr + reelItem + " "
    result = all(item == reelSpun[0] for item in reelSpun)
    if (result):
        winTotal.append(win[reelItem])
    return winTotal

def Main():
    winTotal = []
    moneyWon = 0
    repeat = 1000000
    for i in range(repeat):
        winTotal = play(winTotal)
    for row in winTotal:
        moneyWon = moneyWon + row
    profitTotal = round((0.5*repeat)-moneyWon,2)
    winPercent = len(winTotal)/repeat
    print("In a trial of "+str(repeat)+" slot machine spins:"
        "\nTotal profit: "+str(round((profitTotal/(0.5*repeat)*100),2))+"%",
        "\nProfit per spin: £"+str(round(profitTotal/repeat,2)),
        "\nExpected wins = 0.01%"
        "\nObserved wins = "+str(round(winPercent,2))+"%")

Main()
