# Python is an object oriented programming language
# mostly everything in Python is an object, with its properties and methods
# a class is like an object constructor, or a "blueprint" for creating objects

# a class with a property named x
class myClass:
    x = 5

# use the class to create an object
obj1 = myClass()

# to understand the meaning of classes we have to understand the built-in __init__() function
# all classes have a function called __init__(), which is always executed when the class is being initiated
# use the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person1 = Person("Victory Ma", 21)

def main():
    print(person1.name, person1.age)

if __name__ == "__main__":
    main()