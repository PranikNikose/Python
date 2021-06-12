class Computer:
    def __init__(self):
        self.name = "Pranik"
        self.age  = 21

    def update(self):
        self.name = "PKN"

    def compare(self,other):
        if (self.age == other.age):
            return True
        else:
            return False

c1= Computer()
c2= Computer()
print(c1.name)

c2.update()
print(c2.name)

if c1.compare(c2):   #self.compare(other)
    print("Same")
else:
    print("Diffrent")

if Computer.compare(c1,c2): #class.compare(self,other)
    print("Same")
else:
    print("Diffrent")