class Child:
    def __init__(self, height, behavior):
        self.height = height
        self.behavior = behavior
        self.location = "In Line"
        
    def getHeight(self):
        return self.height
    
    def getBehavior(self):
        return self.behavior
    
    def setLocation(self, location):
        self.location = location
    
    def getLocation(self):
        return self.location
    
    def __eq__(self, other):
        if isinstance(other, Child):
            return (self.height == other.height) and (self.behavior == other.behavior) and (self.location == other.location)
        return False