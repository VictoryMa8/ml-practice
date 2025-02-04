import time

currentTime = time.localtime();

myDict = {
    "name": "Victor",
    "profession": "student",
    "dob": "09-23-2003"
}

mySet = set()
mySet.add("Beep")

def square(x):
    return x * x

def main():
    print("Hello World")
    name = input("Enter your name: ")
    num1 = input("Enter a number: ")
    result = square(int(num1))
    print("Greetings, " + name + ", " + num1 + " squared is " + str(result))
    print("It is currently ", currentTime)
    print(mySet)


if __name__ == "__main__":
    main()