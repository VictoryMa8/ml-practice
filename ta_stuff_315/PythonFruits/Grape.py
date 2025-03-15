from PythonFruits.Fruit import Fruit

class Grape(Fruit):
    def __init__(self, w, s):
        super().__init__(w)
        self.sour = s
        
    def isSour(self):
        return self.sour