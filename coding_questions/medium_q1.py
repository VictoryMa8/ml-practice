'''
Medium Level Coding Questions (Part 1)

1. Smallest Difference
2. Move Element To End
3. Is Monotonic Array
4. Spiral Traverse
5. Longest Peak
6. Array of Products (with division)
7. Merge Overlapping Intervals
8. Best Seat
9. Zero Sum Subarray
10. Missing Numbers
11. Majority Element
12. Sweet and Savory

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

# will add comments later **
def longestPeak(array):
    maxPeak = 0
    currPeak = 1
    rising = False
    falling = False
    for i in range(1, len(array)):
        if array[i] > array[i - 1] and not falling:
            currPeak += 1
            rising = True
        elif array[i] < array[i - 1] and rising:
            currPeak += 1
            falling = True
            maxPeak = max(maxPeak, currPeak)
        elif array[i] > array[i - 1] and falling:
            currPeak = 2
            falling = False
            rising = True
        elif array[i] == array[i - 1]:
            currPeak = 1
            falling = False
            rising = False
    return maxPeak

# will add comments later **
def arrayOfProducts(array):
    result = []
    product = 1
    zeroCount = 0
    
    for i in array:
        if i != 0:
            product *= i
        else:
            zeroCount += 1
    
    for i in array:
        if zeroCount == 0:
            result.append(product / i)

        if zeroCount == 1 and i != 0:
            result.append(0);
        
        if zeroCount == 1 and i == 0:
            result.append(product)
        
        if zeroCount > 1:
            result.append(0)
            
    return result

# more comments later
def mergeOverlappingIntervals(intervals):
    # sort the array by each list's first entry
    intervals.sort(key = lambda x: x[0])
    i = 0
    # iterate through the intervals
    while i < len(intervals) - 1:
        # establish current interval's end and next interval's start
        currEnd = intervals[i][1]
        nextStart = intervals[i + 1][0]
        # if the current end greater than or equal to next start
        if currEnd >= nextStart:
            # let the new end of current be the larger of the two
            # this combines the two intervals
            # say we have [3, 5] and [3, 8], they are overlapping
            # since current interval is the earliest, when we combine, we automatically take it's start
            # since we're combining the two intervals, we must determine with end to take,
            # we use max() to find the largest, put this new interval into current, and delete ther other interval
            newCurrEnd = max(intervals[i][1], intervals[i + 1][1])
            intervals[i][1] = newCurrEnd
            # delete the next interval if they combined
            del intervals[i + 1]
        # otherwise go to the next item
        else:
            i += 1
    return intervals

# will explain later ** 
def bestSeat(seats):
    bestSeatIndex = -1
    currSpace = 0
    bestSpace = 0

    for i in range(len(seats)):
        if seats[i] == 1:
            currSpace = 0
        else:
            currSpace += 1
            if currSpace > bestSpace:
                bestSpace = currSpace
                bestSeatIndex = i - currSpace // 2
    return bestSeatIndex

# will explain later **
def zeroSumSubarray(nums):
    sums = set()
    count = 0
    for number in nums:
        sums.add(count)
        count += number
        if count in sums:
            return True
    return False

# given a list of numbers (nums) from 1 to n, find the two missing numbers in that interval
# this means that the length of nums is n - 2
def missingNumbers(nums):
    # initialize result to return
    result = []
    # create set of nums
    mySet = set(nums)
    # go from 1 to n (or length of nums + 2), we + 3 because range is exclusive
    for i in range(1, len(nums) + 3):
        # if the current number is not in the set, add it to result
        if i not in mySet:
            result.append(i)
    # example: nums = [1, 4], this list is added to the set
    # i visits numbers from 1 to 4 and notices that 2 and 3 are not in the set, this is returned
    return result

# explaining ltr
def majorityElement(array):
    answer = array[0]
    count = 1

    for i in range(1, len(array)):
        if array[i] == answer:
            count += 1
        else:
            count -= 1

        if count == 0:
            answer = array[i]
            count = 1
    return answer

# explaining ltr **
# sorting and using two pointers to traverrse the array
def sweetAndSavory(dishes, target):
    result = [0, 0]
    dishes.sort()
    # first and last elements
    left = 0 
    right = len(dishes) - 1
    bestCombo = float('inf')
    while left < right and dishes[left] < 0 and dishes[right] > 0:
        currCombo = dishes[left] + dishes[right]
        # combo is too savory
        if currCombo > target:
            right -= 1
            continue
        closenessToTarget = target - currCombo
        if closenessToTarget <= bestCombo:
            result[0] = dishes[left]
            result[1] = dishes[right]
            bestCombo = closenessToTarget
        left += 1
    return result


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()