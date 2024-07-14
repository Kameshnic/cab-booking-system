class Driver:
    def __init__(self, id=None, name=None, password=None, phoneNumber=None, carId=None, currentLocation=None, available=None):
        self.id = id
        self.name = name
        self.password = password
        self.phoneNumber = phoneNumber
        self.carId = carId
        self.currentLocation = currentLocation
        self.available = available

    def isNotNull(self):
        return self.id != None and self.name != None and self.password != None and self.phoneNumber != None and self.carId != None and self.currentLocation != None and self.available != None

    def clear(self):
        self.id = None
        self.name = None
        self.password = None
        self.phoneNumber = None
        self.carId = None
        self.currentLocation = None
        self.available = None