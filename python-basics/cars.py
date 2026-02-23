# name : peter mbugua
# date : 23/02/2026
# program to show classes in pyrthon

class Car():
    # attributes of the car
    def __init__(self,model,make,color):
    
        self.model = model
        self.make = make
        self.color = color
    # print car details
    def print_details(self,make,model,color):
        
        print(f"car  details: {make} {model} of color {color}")

#instantiate a class object
my_car = Car("Atenza","Make","Color")
dads_car = Car("Land_cruiser","Toyota","Black")

my_car.print_details("Atenza","Make","Color")

    