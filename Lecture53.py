Amount = 1000
def withdraw(money):
    if money > Amount:
        print("You can not withdraw!")
        return Amount
    else:
        return Amount - money
userWithdraw = int(input("Enter your money that you want to withdraw:"))
result = withdraw(userWithdraw)
print("Your balance is : ",result)