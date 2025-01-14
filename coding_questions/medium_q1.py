'''
Medium Level Coding Questions (Part 1)

1. Smallest Difference
2. Move Element To End
3. Is Monotonic Array

'''

# we are given two arrays, find the pair of two numbers that has the smallest absolute difference
def smallestDifference(arrayOne, arrayTwo):
    # initialize the 'smallest' value to record the best pair
    # the return value is a list named 'closest' that contains the pair
    smallest = float("inf")
    closest = []
    # look at each item in arrayOne
    for i in arrayOne:
        # for each item in arrayOne, look at each item in arrayTwo
        for j in arrayTwo:
            # compute their difference and get the absolute value of that, compare it to smallest
            if abs(i - j) < smallest:
                # if it is smaller than the current 'smallest', name it the new smallest difference
                smallest = abs(i - j)
                # update the list to return
                closest = [i, j]
    return closest

# will add comments later
def moveElementToEnd(array, toMove):
    # sort array asc
    array.sort()
    firstIndex = 0
    lastIndex = 0
    # traverse until you find the first instance of the target int
    for i in range(len(array)):
        if array[i] == toMove:
            firstIndex = i
            break
    # traverse backwards until you find the last instance
    for i in range(len(array) - 1, -1, -1):
        if array[i] == toMove:
            lastIndex = i
            break
    # take out all the instances from first to last index
    extract = array[firstIndex:lastIndex + 1]
    # delete it from the array
    del array[firstIndex:lastIndex + 1]
    # put it back onto the array
    array.extend(extract)
    return array

# will add comments later
def isMonotonic(array):
    if len(array) <= 1:
        return True
    decreasing = True
    increasing = True
    prev = array[0]
    for i in range(1, len(array)):
        if prev > array[i]:
            increasing = False
        elif prev < array[i]:
            decreasing = False
        prev = array[i]
    return decreasing or increasing


# will add comments later **
def spiralTraverse(array):
    result = []
    # while theres stuff still in the array
    while array:
        # take the first row
        result += array.pop(0)
        # rotate the rest of the matrix
        columns = zip(*array)
        new_rows = list(columns)
        array = new_rows[::-1]
    return result

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()