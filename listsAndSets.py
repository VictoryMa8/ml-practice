
# lists allow duplicates, sets automatically remove them

myList = [1, 5, 4, 3, 2]
mySet = {10, 10, 7, 9, 8, 6}
mySet2 = {"bob", "cat", "moose"}

def main():
    # lists support indexing/slicing, sets don't
    print(myList[3])

    # using for item in list
    fruits = ['apple', 'banana', 'cherry']
    for item in fruits:
        item = item.upper()  # this doesn't modify the original list
    print(fruits)  # still apple, banana, cherry

    # using for i in range(len(list))
    for i in range(len(fruits)):
        fruits[i] = fruits[i].upper()  # this DOES modify the list
    print(fruits)  # prints ['APPLE', 'BANANA', 'CHERRY']

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
    print(mySet2)
    mySet2.clear()
    print(mySet2)

    mySet3 = {1, 2, 3}  
    mySet4 = {3, 4, 5}
    # del deletes the set completely
    # union() and update() methods joins all items from both sets.
    print(mySet3.union(mySet4))
    # intersection() method keeps ONLY the duplicates.
    print(mySet3.intersection(mySet4))
    # difference() method keeps the items from the first set that are not in the other set(s).
    print(mySet3.difference(mySet4))
    # symmetric_difference() method keeps all items EXCEPT the duplicates.
    print(mySet3.symmetric_difference(mySet4))

    # all methods
    # https://www.w3schools.com/python/python_sets_methods.asp

if __name__ == "__main__":
    main()
