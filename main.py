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

counter = 0

def main():
    print("Hello World")
    file1 = open("./example.txt", "a")
    file1.write("\n3, Joe, Scientist")
    file1.close()

if __name__ == "__main__":
    main()