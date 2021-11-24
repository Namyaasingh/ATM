print ("welcome")
print ("state bannk of india")
print ("insert your card")
pin=1912 #here we store the pin 
transaction=["balance inquary","withdrawl money","deposite transfer money","change pin","quit"]
amt=50000
pin= int(input("enter your pin to proceed"))
if pin==1912: 
    print("choose your transaction")
    print("1.balance inquary")
    print("2.withdrawl money")
    print("3.deposit money")
    print("4.change pin")
    print("5.transfer money")
    print("6.quit")
    print("transaction")
    transaction =input("transasction:")
    if transaction =="balance inquary":
        print(amt)
        slip =input("do you want slip")
        if slip=="yes":
            print("here is your slip,thanks for your visiting")
        else:
            print("thanks for your visiting") 
    elif transaction=="withdrawl money":
        amount =int(input("enter the amount"))
        if 0<amount <=5000:
            print("collect your cash")
            print("your balance amount is")
            amt-amount
        else:
            print("enter valid amount to cash")
    elif transaction == "deposit money":
        deposit = int (input("your amount to deposit"))
        if 0<deposit <=50000:
            print("your deposit is successfully")
            print ("your updated balance is :",amt+deposit)
        else:
            print("enter valid amount to proceed")
    elif transaction== "change pin":
        new_pin=int(input("enter your pin"))
        if new_pin >0: 
            print("your changing pin is successfully")
        else:
            print("please input valid pin")
    elif transaction== "transfer money":
        transfer = int(input("please enter the your money"))
        if transfer <=amt: 
            print ("your transfered money is successfully")
        else:
            print("please input your valid money")
    elif transaction == "quit":
        quit_1 =input("please a quit")
        if quit_1=="yes":
            print("quit")
        else:
            print("choose any transation please")
    else: 
        print ("wrong pin please try again")