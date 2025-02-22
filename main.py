import time
import re

currentTime = time.localtime();

myDict = {
    "name": "Victor",
    "profession": "student",
    "dob": "09-23-2003"
}

mySet = set()
mySet.add("Beep")
mySet.add("Boop")
mySet.add("Bop")

if "Bop" in mySet:
    mySet.add("Bam")

def next_id(file_path): # take in file
    file_a = open(file_path, "r") # read it
    lines = file_a.readlines() # get each line
    if lines: # if there are lines
        id = lines[-1][0] # get first char of last line (the id, usually)
        return int(id) + 1 # return that + 1
    else:
        return 1 # if empty, establish first id
    
def main():
    print("Hello World")
    print(mySet)
    
    file1 = open("./example.txt", "a") # open file
    next = next_id("./example.txt") # call next_id
    name = input("Enter your name: ")
    profession = input("Enter your profession: ")
    file1.write(f"\n{next}, {name}, {profession}") # write user inputs and next id
    file1.close() # close file

    text1 = "The rain in Morocco"
    x = re.search("^The.*cco$", text1)
    if x:
        print("We have a match.")
    else:
        print("No match.")

if __name__ == "__main__":
    main()