# *Args

# Args are t

# Challenge create a function to take an unlimited amount of arguments and return the sum
def add(*args):
    print(sum(args))
add(1, 2, 3, 4, 5)

# Tutorial wanted a for loop when sum was easier :/
def add2(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)
add2(1, 2, 3, 4, 5)


# Kwargs = Multiple keyword arguments that can have defaults same to positional
# With the class below we set up these key words 

class Car:

    def __init__(self,**kwargs) -> None:
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)

# with the above if we don't include the model it'll fail because we didn't set a default

# With the below it'll just pass a blank if it's not included
class Car:

    def __init__(self,**kwargs) -> None:
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")



# You can also return a default value after the key
class Car:

    def __init__(self,**kwargs) -> None:
        self.make = kwargs.get("make", "Nissan")
        self.model = kwargs.get("model", "GTR")

