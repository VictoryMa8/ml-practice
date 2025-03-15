from PythonFruits.Fruit import Fruit

class Tomato(Fruit):
    def __init__(self, w, m):
        super().__init__(w)
        self.moldy = m
        
    def isMoldy(self):
        return self.moldy