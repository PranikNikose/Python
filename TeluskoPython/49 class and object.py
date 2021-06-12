
class Computer:
    def Config(self):
        print("i5, 8gb ,1TB")


comp1 = Computer()
comp2 = Computer()

Computer.Config(comp1)
Computer.Config(comp2)
print()
comp1.Config()
comp2.Config()


