
# lists allow duplicates, sets automatically remove them

myList = [1, 5, 4, 3, 2]
mySet = {10, 10, 7, 9, 8, 6}

def main():
    # lists support indexing/slicing, sets don't
    print(myList[3])

    # see if an element is in a set O(1)
    print(7 in mySet)

    # once a set is created, you cannot change its items
    # but you can add new items
    mySet.add(20)

    for i in mySet:
        # lists maintain order, sets are unordered
        print(i)

    print("After adding myList to mySet, removing 8, and discarding 20: ")

    # add items from a list, set, etc. to another set with update
    mySet.update(myList)

    # remove items with remove or discard 
    # remove raises an error if the item doesn't exist
    mySet.remove(8)
    mySet.discard(20)

    for i in mySet:
        print(i)

    # pop removes a random item
    print("Using the pop method, we removed", mySet.pop())

    # clear empties the set
    # del deletes the set completely

    # union() and update() methods joins all items from both sets.
    # intersection() method keeps ONLY the duplicates.
    # difference() method keeps the items from the first set that are not in the other set(s).
    # symmetric_difference() method keeps all items EXCEPT the duplicates.

    # all methods
    # https://www.w3schools.com/python/python_sets_methods.asp

if __name__ == "__main__":
    main()