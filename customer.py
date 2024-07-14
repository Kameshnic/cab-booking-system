class Customer:
    def __init__(self, id: int = -1, name: str = "", phoneNumber: str = "", password: str = ""):
        self.id = id
        self.name = name
        self.phoneNumber = phoneNumber
        self.password = password

    def isNull(self): 
        return self.id == -1

    def isNotNull(self): 
        return self.id != -1

    def clear(self):
        self.id = -1
        self.name = ""
        self.phoneNumber = ""
        self.password = ""
