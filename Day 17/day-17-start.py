#################################
# Creating our first empty class#
#################################


class User:  # classes start with Pascal case. Every letter is capitalised. SoThisIsPascal
    pass


user_1 = User()  # instantiates the class using the user_1 variable

# adds attributes to the user_1 this is ok for one offs but for tens, hundreds or thousands of items need creating a constructor is better used.
user_1.id = "001"
user_1.username = "Roberta"


###############################
# Creating a class with a init#
###############################

# the self keyword allows you to refer to things inside the class


class NewUser:  # classes start with Pascal case. Every letter is capitalised. SoThisIsPascal
    def __init__(self, id, username) -> None:
        self.id = id
        self.username = username
        self.followers = 0  # As all users would start at 0 followers no need to ask for it to be passed through as a parameter
        print(f"Creating a new user...{id}")


user_001 = NewUser("001", "Roberta")
user_002 = NewUser("002", "Jack")


###########################################################
# Classes with methods(a function inside a class) as well #
###########################################################


class Car:
    def __init__(self) -> None:
        self.seats = 5  # default amount of seats in a car

    def racemode(
        self,
    ):  # this function can be called to change the amount of seats associated
        self.seats = 2


car = Car()  # sets up the object
print(f"Our car has {car.seats}")  # shows there's 5 seats
car.racemode()  # calls the function
print(f"Racemode activated! Car now has {car.seats} seats")  # now there's 2!

# Another example


class User2:  # classes start with Pascal case. Every letter is capitalised. SoThisIsPascal
    def __init__(self, id, username) -> None:
        self.id = id
        self.username = username
        self.followers = 0  # As all users would start at 0 followers no need to ask for it to be passed through as a parameter
        self.following = 0  # As everyone would start following no one at the start..
        print(f"Creating a new user...{id}")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_001 = User2("001", "Roberta")
user_002 = User2("002", "Jack")

user_001.follow(user_002)
print(user_001.followers)  # 0
print(user_001.following)  # 1
print(user_002.followers)  # 1
print(user_002.following)  # 0
