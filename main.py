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

def next_id(file_path):
    file_a = open(file_path, "r")
    lines = file_a.readlines()
    if lines:
        id = lines[-1][0]
        return int(id) + 1
    else:
        return 1
    
def main():
    print("Hello World")
    file1 = open("./example.txt", "a")
    next = next_id("./example.txt")
    name = input("Enter your name: ")
    profession = input("Enter your profession: ")
    file1.write(f"\n{next}, {name}, {profession}")
    file1.close()

if __name__ == "__main__":
    main()