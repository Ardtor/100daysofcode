class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    
    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self) -> None: #without this the class would not have access to the methods from animal
        super().__init__()

    def breathe(self):
        super().breathe() #this will Copy everything from the animal.breathe() and then add extra
        print("doing this under water")

    def swim(self):
        print("moving in water")

nemo = Fish() 
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)



