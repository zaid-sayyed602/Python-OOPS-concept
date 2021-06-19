#import mymodule
from mymodule import vehicle
obj1=vehicle()
choice=0
while(True):
    print("1.ASK")
    print("2.PRINT")
    print("3.UPDATE")
    print("4.Exit")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        obj1.asktype()
    elif(choice==2):
        obj1.print()
    elif(choice==3):
        enter=input("What you want to update\n")
        if(enter=="name"):
            obj1.updatename()
        elif(enter=="type"):
            obj1.updatetype()
        elif(enter=="colour"):
            obj1.updatecolour()
        elif(enter=="model"):
            obj1.updatemodel()
        else:
            print("Bad command")
    elif(choice==4):
        print("EXITED")
        break
    else:
        print("BAD COMMAND")
