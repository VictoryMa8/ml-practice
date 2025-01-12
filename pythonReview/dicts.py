# dictionaries are used to store data values in key-value pairs

# a dictionary is ordered, changeable, and does not allow duplicates

myDict = {
    "name": "Victory Ma",
    "edu": "St. Olaf College",
    "favFood": "Fried Chicken",
    "age": 21,
    "asian": True
}

def main():
    # print the value from a key
    print(myDict["name"])

    # print the length of a dict
    print(len(myDict))

    # use a constructor to create a dict
    person = dict(name = "John Doe", age = 30, country = "United States")
    print(person)

    # see all keys
    print("They keys of myDict:", myDict.keys())

    # see all values
    print("They values of myDict:", myDict.values())

    # change the value of a key
    myDict["favFood"] = "Ramen"

    # add a key-value pair
    myDict["goodLooks"] = 100

    # get all items in a dict as tuples in a list
    print(myDict.items())

    # check if a key is in the dict
    if "name" in myDict:
        print("Yes, the key 'name' is in myDict")

    # remove an item with pop or del
    myDict.pop("asian")
    del myDict["goodLooks"]
    print(myDict.keys())

    # can also use del to delete the entire dictionary
    messageDict = {
        "message": "Hello!"
    }
    print(messageDict)
    del messageDict

    # clear all items from dictionary
    coolDict = {
        "state": "Minnesota"
    }
    coolDict.clear()
    print(coolDict)

    # traverse through dict

    for i in myDict:
        print("Item:", i, myDict[i])

    # setdefault returns the value of the specified key
    # if the key does not exist, then insert the key with the specified value

    x = myDict.setdefault("major", "Computer Science")
    print(x)

    # all methods: https://www.w3schools.com/python/python_dictionaries_methods.asp

if __name__ == "__main__":
    main()