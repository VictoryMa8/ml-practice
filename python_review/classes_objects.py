# Python is an object oriented programming language
# mostly everything in Python is an object, with its properties and methods
# a class is like an object constructor, or a "blueprint" for creating objects

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
        return f"This person is {self.name}, who is {self.age} years old."
    
person1 = Person("Victory Ma", 21)

def main():
    print(person1)

if __name__ == "__main__":
    main()