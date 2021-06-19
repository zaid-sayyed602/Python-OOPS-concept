import pymysql as con
try:
    db=con.connect(
        host="localhost",
        user="root",
        password="root",
        database="shop")
    print("Connection success")
    cur=db.cursor()
except:
    print("something wrong in the connection")
class cart1:
    def add(self):
        print("-x-x-x-x-ITEMS IN SHOP-x-x-x-x-x")
        select="select * from grocery"
        cur.execute(select)
        shop=cur.fetchall()
        for shop1 in shop:
            name=shop1[1]
            price=shop1[2]
            print("Item Name=",name,"Item Price=",price,"\n")
        for i in range(int(input("Enter the no of items you want\n"))):      
            self.name=input("Enter the name of the item ypu want\n")
            self.quantity=int(input("Enter the quantity\n"))
            flag=0
            for i in range(len(shop)):
                if(self.name==shop[i][1]):
                    insert="insert into user values(%s,%s,%s)"
                    value=[0,self.name,self.quantity]
                    cur.execute(insert,value)
                    db.commit()
                    print("Successfully added to cart")
                    flag=1
            if(flag==0):
                print("NOT in the shop")
    def remove(self):
        self.remname=input("Enter the name of the item you want to remove\n")
        select="select * from user where item=%s"
        value=[self.remname]
        cur.execute(select,value)
        cart=cur.fetchall()
        print(cart)
        flag=0
        for i in range(len(cart)):
            if(cart[i][1]==self.remname):
                delete="delete from user where item=%s"
                value=[self.remname]
                cur.execute(delete,value)
                db.commit()
                print("Deleted successfully")
                flag=1
        if(flag==0):
            print("NOt in the cart")      
    def update(self):
        self.name=input("Enter the name of the item\n")
        self.quantity=int(input("Enter the quantity\n"))
        select="select * from user"
        cur.execute(select)
        cart=cur.fetchall()
        flag=0
        for i in range(len(cart)):
            if(cart[i][1]==self.name):
                update="update user set quantity=%s where item=%s"
                value=[self.quantity,self.name]
                cur.execute(update,value)
                db.commit()
                print("Updated Successfully")
                flag=1
        if(flag==0):
            print("NOT IN THE CART")

    def bill(self):
        select="select * from grocery"
        cur.execute(select)
        shop=cur.fetchall()
        select="select * from user"
        cur.execute(select)
        cart=cur.fetchall()
        self.cnt=0
        for i in range(len(cart)):
            for j in range(len(shop)):
                if(cart[i][1]==shop[j][1]):
                    self.cnt+=cart[i][2]*shop[j][2]
                    print(cart[i][1],"=",cart[i][2]*shop[j][2],"/-")
        print("TOTAL BILL IS",self.cnt)
obj=cart1()
choice=0
while(True):
    print("1.ADD ITEMS TO THE CART")
    print("2.REMOVE FORM THE CART")
    print("3.UPDATE")
    print("4.BILL")
    print("5.EXIT")
    choice=int(input("Enter your choice\n"))
    if(choice==1):
        obj.add()
    elif(choice==2):
        obj.remove()
    elif(choice==3):
        obj.update()        
    elif(choice==4):
        obj.bill()        
    elif(choice==5):
        print("Exited")
        break
    else:
        print("INCORRECT INPUT")
