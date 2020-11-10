menuList = []
priceList = []
def ShowBill():
    print("Recipe".center(20,"-"))
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])

def TotalPrice():
    total = 0
    for price in priceList:
        total += int(price)
    print("Total : %.2f Bath"%total)

while True:
    menuName = input("Please Enter the menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)
ShowBill()
TotalPrice()