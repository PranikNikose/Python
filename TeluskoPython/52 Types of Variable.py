
class Car:
    wheels = 4              # Class Variable or static variable

    def __init__(self):     # Attributes
        self.milage=10      # instance Variable or object variable
        self.company="BMW"  # instance Variable or object variable

    def update(self):       # Update Method  #Behaviour
        self.milage=15

c1=Car()     # Assigning object = class
c2=Car()

c2.update()

print(c1.company, c1.milage,c1.wheels)
print(c2.company, c2.milage,c2.wheels)

