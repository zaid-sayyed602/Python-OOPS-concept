import vehicle_module
#from mymodule2 import vehicle
obj=vehicle_module.vehicle()
choice=0
while(True):
    print("1.ADD CAR")
    print("2.REMOVE ")
    print("3.UPDATE")
    print("4.EXIT")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        obj.add()
    elif(choice==2):
        obj.remove()
    elif(choice==3):
        obj.update()        
    elif(choice==4):
        obj.dbclose()
        print("Exited")
        break
    else:
        print("INCORRECT INPUT")
    
