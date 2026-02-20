# DRY => Do not repeat y
# ourself

"""

 class:  blueprint of an object
 object is an instance of a class: 
    - inheritance
    - polymorphism
    - encapsulation
"""

class Bottle:
    shape = "hour-glass"

    # attributes - intialization
    def __init__(self, size, color, material, brandName):
        self.size = size 
        self.color = color
        self.__brandName =brandName # encapsulation => makes brandname private only accessible to class bottle
        self.material = material 
    
    # methods
    def checkTemperature(self):
        print(f"your {self.material}'s temperature is ok, it is at RTP!")

    def getBrandName(self):
        print(f"Our brand is called: {self.__brandName}")


#  creating the objects
sodaBottle = Bottle(1000, "blue","glass", "Coca-cola")
sodaBottle2 = Bottle(800, "black", "aluminium", "Pepsi")
# print(sodaBottle.shape)
# sodaBottle.checkTemperature()
# sodaBottle.getBrandName()
# print("===========================")
# print(sodaBottle2.shape)
# sodaBottle2.checkTemperature()
# sodaBottle2.getBrandName()
# print(sodaBottle.brandName) 


"""
Inheritance: 
 -  it is the process of getting all methods and attributes from th eparent class to the child class
 - the famous statement "huyo ni kama mama wake or baba wake"

"""


class Human:
#  the moment i create this object, this is the first thing i initalize
    def __init__(self, name, height, hobby):
        self.name = name
        self.height = height 
        self.hobby = hobby    
    #  behaviors => funtions, those that reside inside a class are called methods
    def eatFood(self):
        print(f"{self.name} is devouring food! while enjoing their {self.hobby} hobby") 
 
    def workout(self):
        print(f"{self.name}, does squats on Friday's")

    def cooking(self):
        print(f"{self.name} is cooking eggs! ")

class Athlete(Human):

    def __init__(self,name, height, hobby, age):
        super().__init__(name, height, hobby)
        self.age = age

    def training(self):
        print(f"{self.name} trains 6 times a weeek")

    def competitions(self):
        print(f"{self.name} is competing in the olympics 2050")


human1 = Human("Joy", 134, "reading") # created an object -> a Human being
human1.eatFood() # calling the functions related to the human being
human1.cooking() # calling the functions related to the human being
human1.workout() # calling the functions related to the human being

print("======================================================")

#  child of Human
athlete1 = Athlete("Jane", 140, "cooking", 19)
athlete1.cooking()
athlete1.training()


print("===========================================")

name = "Marie Curie" # string
print(len(name))

fruits = [ "apple", "mango", "pawpaw", "banana"] # list

print(len(fruits))

memberList = {"A", "B", "C", "D", "E", "F","G"} # set
members = memberList # set

print(len(members))
print("===========================================")