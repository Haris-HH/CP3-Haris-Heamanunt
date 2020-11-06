number = int(input("Enter a number :"))
space = number
for i in range(number):
    space -= 1
    print(" "*space,"*"*((i*2)+1))