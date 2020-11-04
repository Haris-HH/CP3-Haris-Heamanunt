userName = input("Username : ")
userPassword = input("Password : ")
if(userName == "Test" and userPassword == "Test123"):
    print("---Welcome---")
    print("1.Pen        35 Bath")
    print("2.Note       10 Bath")
    userSelected = int(input("Please select number of product: "))
    if(userSelected == 1):
        print("You selected Pen")
        productQuantity = int(input("How many do you want? : "))
        print("Total: Pen ",productQuantity," x 35 = ",productQuantity*35," Bath")
        print("Thankyou")
    elif(userSelected == 2):
        print("You selected Note")
        productQuantity = int(input("How many do you want? : "))
        print("Total: Note ",productQuantity," x 10 = ",productQuantity*10," Bath")
        print("Thankyou")
    else:
        print("You have enter the wrong number!!")