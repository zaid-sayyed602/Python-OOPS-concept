
class vehicle:
    def asktype(self):
        self.name=input("Enter the name of the vehicle\n")
        self.vehicletype=input("Enter the type of the vehicle\n")
        self.colour=input("Enter the colour of the vehicle\n")
        self.model=input("Enter the model of the vehicle\n")
    def print(self):
        print(self.name)
        print(self.vehicletype)
        print(self.colour)
        print(self.model)
    def updatename(self):
        self.name=input("Enter the name of the vehicle\n")
    def updatetype(self):
        self.vehicletype=input("Enter the type of the vehicle\n")
    def updatecolour(self):
        self.colour=input("Enter the colour of the vehicle\n")
    def updatemodel(self):
        self.model=input("Enter the model of the vehicle\n
