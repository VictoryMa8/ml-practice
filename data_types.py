import random

# text: str
myStr = "Hello World"

# numeric: int, float, complex
myInt = 4
myFloat = 1.24901
myComplex = 1j

# sequence: list, tuple, range
myList = [1, 5, 4, 3] 
myTuple = ("apple", "banana", "cherry")
myRange = range(5)

# mapping: dict
myDict = {
    "id": 5,
    "name": "Bob",
    "job": "Full-Stack Web Developer"
}
# set: set, frozenset
mySet = {"watermelon", "mango", "durian"}
myFrozenSet = frozenset({"watermelon", "mango", "durian"})

# boolean: bool
myBool = True
myBool2 = False

# binary: bytes, bytearray, memoryview
myBytes = b"Hello"
myByteArray = bytearray(5)
myMemoryView = memoryview(bytes(5))
# none:	nonetype
myNoneType = None

myMultilineStr = """This is an example
of a multiline string, you have to use three single quotes or 
three double quotes
like this."""

# in python, a string is single char is just a string of length 1
# square brackets can access elements of the string
name = "Victory Ma"

whitespaceExample = "  Hello  ...  "

def main():

    print(random.randrange(1, 10)) # prints a random number between 1 and 9

    print(myMultilineStr)

    print(name[6]) # prints y

    # loop through chars of a str (remember newline char at the end of each print)
    for i in name:
        print(i)

    # get the length of a str
    print(len(name))

    # check if a certain phrase is present in a string
    # is "tor" in Victory Ma?
    print("tor" in name) # prints true
    if "Vic" in name:
        print("Yep, 'Vic' is in the 'Victory Ma'")

    # check if a phrase isn't in the string
    if "aghh" not in name:
        print("No, 'aghh' is not in 'Victory Ma'")

    # return a range of chars by using slice
    print(name[0:6]) # prints Victor from Victory Ma (exclusive of name[6])

    # use negative slicing to start at the end
    print(name[-5:-1]) # prints "ry M" r (-4) y (-3) (space) (-2) M (-1), it is exclusive of -5

    # uppercase/lowercase an entire string
    print(name.upper()) # "VICTORY MA"
    print(name.lower()) # "victory ma" (original string: Victory Ma)

    # remove whitespace at beginning and end of string
    print(whitespaceExample)
    print(whitespaceExample.strip())

if __name__ == "__main__":
    main()