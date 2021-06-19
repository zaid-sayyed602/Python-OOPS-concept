shop=[["oil",50],["rice",40],["wheat",60],
      ["oats",100],["corn",50],["maggi",70],
      ["maida",120],["coke",80],["flour",30],
      ["ice",30]]
cart=[]
class cart1:
    def add(self):
        print("-x-x-x-x-ITEMS IN SHOP-x-x-x-x-x")
        for shop1 in shop:
            name=shop1[0]
            price=shop1[1]
            print("Item Name=",name,"Item Price=",price,"\n")
        for i in range(int(input("Enter the no of items you want\n"))):      
            self.name=input("Enter the name of the item ypu want\n")
            self.quantity=int(input("Enter the quantity\n"))
            flag=0
            for i in range(len(shop)):
                if(self.name==shop[i][0]):
                    temp=[self.name,self.quantity]
                    cart.append(temp)
                    print(cart)
                    flag=1
            if(flag==0):
                print("NOT in the shop")
    def remove(self):
        self.remname=input("Enter the name of the item you want to remove\n")
        flag=0
        for i in range(len(cart)):
            if(cart[i][0]==self.remname):
                cart.remove(cart[i])
                print("removed successfully\n")
                print(cart)
                flag=1
        if(flag==0):
            print("NOt in the cart")                
    def bill(self):
        self.cnt=0
        for i in range(len(cart)):
            for j in range(len(shop)):
                if(cart[i][0]==shop[j][0]):
                    self.cnt+=cart[i][1]*shop[j][1]
                    print(cart[i][0],"=",cart[i][1]*shop[j][1],"/-")
                    print("TOTAL BILL IS",self.cnt)
obj=cart1()
choice=0
while(True):
    print("1.ADD ITEMS TO THE CART")
    print("2.REMOVE FORM THE CART")
    print("3.BILL")
    print("4.EXIT")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        obj.add()
        print("his is temp1",temp1)
    elif(choice==2):
        obj.remove()
    elif(choice==3):
        obj.bill()        
    elif(choice==4):
        print("Exited")
        break
    else:
        print("INCORRECT INPUT")
