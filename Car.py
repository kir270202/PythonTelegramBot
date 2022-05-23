class Car:
    def __init__(self):
        self.transmission = ""
        self.bodyStyle = ""
        self.wheelDrive = ""
        self.price = ""
        self.fuelType = ""
        self.steeringWheelType = ""
        self.color = ""
        self.milage = ""
        self.horsepowerLowerBound = ""
        self.horsepowerUpperBound = ""
        self.UrlResult = ""

    #Setters

    def setTransmission(self, transmission):
        self.transmission = transmission

    def setBodyStyle(self, bodyStyle):
        self.bodyStyle = bodyStyle

    def setWheelDrive(self, wheelDrive):
        self.wheelDrive = wheelDrive

    def setPrice(self, price):
        self.price = price

    def setFuelType(self, fuelType):
        self.fuelType = fuelType

    def setSteeringWheelType(self, steeringWheelType):
        self.steeringWheelType = steeringWheelType

    def setColor(self, color):
        self.color = color

    def setMilage(self, milage):
        self.milage = milage

    def setHorsepowerLowerBound(self, horsepowerLowerBound):
        self.horsepowerLowerBound = horsepowerLowerBound

    def setHorsepowerUpperBound(self, horsepowerUpperBound):
        self.horsepowerUpperBound = horsepowerUpperBound

    def setUrlResult(self, UrlResult):
        self.UrlResult = UrlResult


    #Getters
    def getTransmission(self):
        return self.transmission

    def getBodyStyle(self):
        return self.bodyStyle

    def getWheelDrive(self):
        return self.wheelDrive

    def getPrice(self):
        return self.price

    def getFuelType(self):
        return self.fuelType

    def getSteeringWheelType(self):
        return self.steeringWheelType

    def getColor(self):
        return self.color

    def getMilage(self):
        return self.milage

    def getHorsepowerLowerBound(self):
        return self.horsepowerLowerBound

    def getHorsepowerUpperBound(self):
        return self.horsepowerUpperBound

    def getUrlResult(self):
        return self.UrlResult