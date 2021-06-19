import coursestudent
obj=coursestudent.course()
obj1=coursestudent.student()
choice=0
while(True):
    print("1.ADMIN PANEL")
    print("2.USER PANEL")
    print("3.EXIT")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        print("\--ADMIN LOGIN--/")
        lname=input("Enter Username\n")
        lpass=input("Enter password\n")
        if(lname=="root" and lpass=="root"):
            print("login Success")
            while(True):
                choice1=0
                print("1.PRINT COURSE")
                print("2.ADD COURSE")
                print("3.UPDATE COURSE")
                print("4.REMOVE COURSE")
                print("5.BACK TO MAIN MENU")
                choice1=int(input("Enter your choice\n"))
                if(choice1==1):
                    obj.printcourse()
                elif(choice1==2):
                    obj.addcourse()
                elif(choice1==3):
                    obj.updatecourse()
                elif(choice1==4):
                    obj.removecourse()
                elif(choice1==5):
                    print("EXITED TO MAIN MENU")
                    break
                else:
                    print("invalid input")
        else:
            print("login failed")
    elif(choice==2):
        while(True):
            choice1=0
            print("1.PRINT STUDENTS")
            print("2.ADD STUDENT")
            print("3.UPDATE STUDENT")
            print("4.REMOVE STUDENT")
            print("5.BACK TO MAIN MENU")
            choice1=int(input("Enter your choice\n"))
            if(choice1==1):
                obj1.printstudent()
            elif(choice1==2):
                obj1.addstudentcourse()
            elif(choice1==3):
                obj1.updatestudentcourse()
            elif(choice1==4):
                obj.removestudentcourse()
            elif(choice1==5):
                print("EXITED TO MAIN MENU")
                break
            else:
                print("invalid input")
    elif(choice==3):
        print("EXITED")
        break
    else:
        print("INVALID INPUT")
