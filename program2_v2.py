#Create a program that will ask how many apples and oranges you want to buy.
#Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
#Display the output in the following format.
#The total amount is ______.

def getApple():
    _apple= input("Please indicate how many apples you want to purchase: ")
    return _apple

def getOrange():
    _orange= input("Please indicate how many oranges you want to purchase: ")

#steps
#1. state price of apple.
appleprice= getApple()
#2. state price of orange.
orangeprice= getOrange()
#3. display total amount.