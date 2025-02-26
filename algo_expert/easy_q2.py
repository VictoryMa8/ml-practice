'''
Easy Level Coding Questions (Part 2)

1. Remove Duplicates From Linked List
2. Middle Node
3. Get Nth Fibonacci
4. Product Sum
5. Binary Search
6. Find Three Largest Numbers
7. Bubble Sort
8. Insertion Sort
9. Selection Sort
10. Is Palindrome
11. Caesar Cipher Encryptor
12. Run Length Encoding
13. Common Characters
14. Generate Document
15. First Non-repeating Character

'''

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

# swap items until all pairs of numbers are i < i+1 while keeping track of swaps
# once we dont have to swap, we end the traversal
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

# insertion sort has us traverse the array, if "next item" is < the "current" item,
# move it down until that is no longer the case
# we keep track of sorted size until we go through the whole thing
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

# in selection sort, we make a new array and traverse the og array and find the min value and add it,
# until we run out of numbers, it is O(n^2)
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

# in a caesar cipher, we take the alphabet, and shift "right" x times, with x being the key
# for example, if we have "abc", and put it through with a key of 3, we would have "def"
# if the key is greater than the amount of letters in the alphabet, wrap back around to abcd etc...
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
        # modulo 26 (-26 until it is less than 26), so it "wraps" around the alphabet
        if newLetterIndex > 25:
            newLetterIndex = newLetterIndex % 26
        # add the new letters to the new string
        newString += a[newLetterIndex]
    return newString

# say we have strings like AAAABBBBCCC, we want to look like this: 4A4B3C, numbers denoting amount of the letter
# if we have more than 9 in a row, we have to do it like this: 9A3A = 12 A's in a row
def runLengthEncoding(string):
    # initialize a result string and a count string
    result = ""
    count = 0
    # traverse string
    for i in range(len(string)):
        # establish current char
        curr = string[i]
        # add 1 to the count
        count += 1
        # if we're at the end of the string, add the current count and char to the result
        if i+1 == len(string):
            result += str(count) + curr  
        # if the count is at 9, stop and add count and char and reset the count
        elif count == 9:
            result += str(count) + curr
            count = 0
        # if the next char does not match current char, add the count with char and reset the count
        elif string[i+1] != curr:
            result += str(count) + curr
            count = 0
    return result

# will explain later
def commonCharacters(strings):
    # make set of one of the strings, in this case the first one
    commonChars = set(strings[0])
    # traverse array of strings
    for string in strings:
        # make a set for chars in common
        inCommonSet = set()
        # look through all chars of current str
        for char in string:
            # if current str has a char in common with the previous set,
            # add it to the compareCurr set
            if char in commonChars:
                inCommonSet.add(char)
        # "reduce" the og set to this new set of chars that are in common
        # between the current str and previous str
        commonChars = inCommonSet
    return list(commonChars)

# generate a document by using the chars in the "characters" string
# the "document" string is what we want to achieve
# example: "ictorrr VVV" can generate the "Victor" document since it has the required chars (more than enough)
def generateDocument(characters, document):
    # create dicts for each string
    charDict = dict()
    docDict = dict()
    # if document string is empty just return true, we can always achieve that
    if document == "":
        return True
    # traverse chars in characters
    for i in characters:
        # add it into the dict or add to the count
        if i not in charDict:
            charDict[i] = 1
        else:
            charDict[i] += 1
    # same with document string
    for i in document:
        if i not in docDict:
            docDict[i] = 1
        else:
            docDict[i] += 1
    # traverse all the counts
    for i in docDict:
        # if any char in document is not in characters, return false, since we can't make the doc
        if i not in charDict:
            return False
        # if at any point the doc needs more instances of a char than we have at our disposal, we can't make the doc
        elif docDict[i] > charDict[i]:
            return False
    # otherwise return true if everything is all good
    return True

# will explain later
def firstNonRepeatingCharacter(string):
    chars = set()
    discard = set()
    for i in string:
        if i not in chars and i not in discard:
            chars.add(i)
        elif i in chars and i not in discard:
            chars.remove(i)
            discard.add(i)
    if len(chars) == 0:
        return -1
    result = 999
    for i in list(chars):
        if string.index(i) < result:
            result = string.index(i)
    return result

def main():
    print("Hello")

if __name__ == "__main__":
    main()