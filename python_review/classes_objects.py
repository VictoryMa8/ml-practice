'''
- Python is an object oriented programming language
- mostly everything in Python is an object, with its properties and methods
- a class is like an object constructor, or a "blueprint" for creating objects
'''


# a class with a property named x
class myClass:
    x = 5

# use the class to create an object
obj1 = myClass()

# all classes have a function called __init__(), which is always executed when the class is being initiated
class Person:
    # use the __init__() function to assign values to object properties,
    # or other operations that are necessary to do when the object is being created
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # the __str__() function controls what is returned when the class object is represented as a string
    
    def __str__(self):
        return f"This person is {self.name}."
    
    # objects can also contain methods
    # methods in objects are functions that belong to that object

    def displayAge(self):
        print(f"The age of {self.name} is {self.age}")
    
person1 = Person("Victory Ma", 21)

'''
- inheritance allows us to define a class that inherits all the methods and properties from another class
- the parent class is the class being inherited from, also called base class
- child class is the class that inherits from another class, also called derived class
'''

class Student(Person):
  def __init__(self, name, age, year):
    # super() function that will make the child class inherit all the methods and properties from its parent
    super().__init__(name, age)
    # here we add a new property to the 'student' class that is not in the 'person' class
    self.graduationYear = year

person2 = Student("Joe Bob", 21, 2026)

def main():
    print(person1)
    person1.displayAge()
    person2.displayAge()
    print(person2.graduationYear)

if __name__ == "__main__":
    main()