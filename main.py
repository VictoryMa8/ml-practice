import time

currentTime = time.localtime();

def square(x):
    return x * x

def main():
    print("Hello World")
    name = input("Enter your name: ")
    num1 = input("Enter a number: ")
    result = square(int(num1))
    print("Greetings, " + name + ", " + num1 + " squared is " + str(result))
    print("It is currently ", currentTime)


if __name__ == "__main__":
    main()