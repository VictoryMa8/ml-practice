# we have a linked list sorted in ascending order
# remove all duplicates from it
# we just go through the linked list see compare the current node to the next node
# since its sorted, we can go node by node and check to see if they're equal
# if they are, just make the current node point to the next next node
def removeDuplicatesFromLinkedList(linkedList):
    # important to note that the linked list is sorted
    # initialize head node
    curr = linkedList
    # while we're not at the end
    while curr.next is not None:
        # if current node's value is equal to the next value
        if curr.value == curr.next.value:
            # make current node point to the next node
            curr.next = curr.next.next
        else:
            # otherwise, just go to the next node
            curr = curr.next
    return linkedList

# find the middle node, if the length if even, get the 'middle-right' node
# fast traveses the linked list 'twice as fast', so by the time the while loop is done iterating,
# the slow one is at the middle point
# make sure the condition still goes if fast.next is not None
# that way we reach the end even if we go past the end 
def middleNode(linkedList):
    # set up two things to traverse the linked list
    slow = linkedList
    fast = linkedList

    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow

# fibonacci sequence
# we have our starting numbers
# iterate until n - 1 exclusive
# we store lastlast number in temp, last number in x and next number in y
def getNthFib(n):
    # first numbers of the sequence are 0, 1
    # the nth number is the sum of the (n - 1)th and (n - 2)th numbers
    # so the 2nd number is 0 + 1 = 1, 3rd is 1 + 1 = 2
    x = 0
    y = 1
    # n - 2, n - 1, and n
    for i in range(n - 1):
        temp = x # 0 1 1 2 3
        x = y # 1 1 2 3 5
        y += temp # 1 2 3 5 8

    return x

# will add more comments later
def productSumHelper(array, depth):
    sum = 0
    for i in array:
        if type(i) == int:
            sum += depth * i
        elif type(i) == list:
            sum += depth * productSumHelper(i, depth + 1)
        else:
            print("Not valid type")
    return sum

def productSum(array):
    return productSumHelper(array, 1)

# in a sorted array, binary search eliminates half the array at a time to find a target
def binarySearch(array, target):

    # establish window (left most item 0, right most is last index)
    left = 0
    right = len(array) - 1
    
    # while we have space to search
    while left <= right:
        # middle is self explanatory
        middle = (left + right) // 2
        if array[middle] == target:
        # if we're looking at the target, retrn it
            return middle
        # if the target is to the right (its bigger), make left 'wall' = middle + 1 (we alr checked middle)
        elif array[middle] < target:
            left = middle + 1
        # if target is smaller (to the left), make right 'wall' = middle - 1 (again, we checked middle)
        else: # array[middle] > target
            right = middle - 1
    return -1

# will explain later
def findThreeLargestNumbers(array):
    max1 = max2 = max3 = -999
    for i in range(len(array)):
        if array[i] > max3:
            max1 = max2
            max2 = max3
            max3 = array[i]
        elif array[i] > max2:
            max1 = max2
            max2 = array[i]
        elif array[i] > max1:
            max1 = array[i]
    return [max1, max2, max3]

# will explain later
def bubbleSort(array):
    numSwaps = 1
    while numSwaps > 0:
        numSwaps = 0
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                numSwaps += 1
    return array

# will explain later
def insertionSort(array):
    i = 0
    sortedSize = 1;
    while sortedSize < len(array):
        nextItem = array[sortedSize]
        i = sortedSize - 1
        while i >= 0 and nextItem < array[i]:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = nextItem;
        sortedSize += 1

    return array

# will explain later
def selectionSort(array):
    tempArr = []
    m = len(array)
    while m > 0:
        minEl = min(array)
        tempArr.append(minEl)
        array.remove(minEl)
        m -= 1
    return tempArr

# will explain later
def isPalindrome(string):
    # set left to traverse one way and right to the other way
    left = 0
    right = len(string) - 1

    # base case if string is one character
    if left == right:
        return True

    # while we look at each character
    while left <= right:
        # if the sides are not exactly the same, return false
        if string[left] != string[right]:
            return False
        # continue to look if characters are the same
        elif string[left] == string[right]:
            # if we reach the end and the string has a equal number of chars
            # example: teet, the pointers look at e and e at the end
            if len(string) % 2 == 0 and left == right - 1:
                return True
            # if we reach the end and the string has an odd number of chars
            # example: popop, the pointers look at the middle p at the end
            elif len(string) % 2 == 1 and left == right:
                return True
            left += 1
            right -= 1

# same thing
def caesarCipherEncryptor(string, key):
    # the letter a = a[0], letter z = a[25]
    a = "abcdefghijklmnopqrstuvwxyz"
    newString = ""
    # traverse the string
    for i in string:
        # get the index of old letter
        letterIndex = a.index(i)
        # calculate the index of the new letter
        newLetterIndex = letterIndex + key
        # if index is over the length of the alphabet,
        # -26 until it is less than 26, so it "wraps" around the alphabet
        while newLetterIndex > 25:
            newLetterIndex = newLetterIndex - 26
        # add the new letters to the new string
        newString += a[newLetterIndex]
    return newString

def main():
    print("Hello")

if __name__ == "__main__":
    main()