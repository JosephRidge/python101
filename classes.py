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
