
def getMoney():
    amountM= float(input("How much money do you have? "))
    return amountM

def getApple():
    appleprice= float(input("What is the price of an apple per piece? "))
    return appleprice

def getChange():
    change = float(money % appleP)
    return change


def getAmount(money, appleP):
    maxnoApl= int(money // appleP)
    return maxnoApl


money= getMoney()

appleP= getApple()
_change= getChange()
totalamount= getAmount(money, appleP)

print(f"You can buy {totalamount} apples and your change is PHP{_change: .2f}")