class vehicle:
    def input(self,name,vehicletype,colour,model):
        self.name=name
        self.vehicletype=vehicletype
        self.colour=colour
        self.model=model
obj1=vehicle
name=input("enter the name of the vehicle\n")
vehicletype=input("enter the type of the vehicle\n")
colour=input("enter the colour of the vehicle\n")
model=input("enter the model of the vehicle\n")
obj1.input(name,vehicletype,colour,model)
print(obj1.name)
print(obj1.vehicletype)
print(obj1.colour)
print(obj1.model)
