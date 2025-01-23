'''
Medium & Hard Level Coding Questions (Part 2)

1. Reverse Linked List
2. Quick Sort
3. Ways To Make Change (Infinite Supply)
4. Minimum Number Of Coins For Change
5. Number Of Ways To Traverse Graph
6. Kadane's Algorithm
7. Single Cycle Check
8. Breadth First Search
9. Merge Sort
10. Knapsack Problem

'''

# 1. Reverse Linked List
def reverseLinkedList(head):
    # 1 -> 5 -> 3 -> 7 -> 9
    previousNode = None
    currentNode = head # 1
    while currentNode is not None:
        nextNode = currentNode.next # nextNode = currentNode.next = 5
        currentNode.next = previousNode # currentNode.next = None
        previousNode = currentNode # previousNode = currentNode = 1
        currentNode = nextNode # currentNode = nextNode = 5
    return previousNode

# 2. Quick Sort
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, start, stop):

	if stop <= start:
		return

	pivot = array[stop]
	i = start
    
	for j in range(start, stop + 1):
		if array[j] <= pivot:
			array[i], array[j] = array[j], array[i]
			i += 1
            
	quickSortHelper(array, start, i - 2)
	quickSortHelper(array, i, stop)
	return

# 3. Ways To Make Change (Infinite Supply)
def numberOfWaysToMakeChange(n, denoms):
    ways = [0] * (n + 1)
    ways[0] = 1

    for i in denoms:
        for j in range(1, n + 1):
            if i <= j:
                ways[j] += ways[j - i]
    return ways[n]

# 4. Minimum Number Of Coins For Change
def minNumberOfCoinsForChange(n, denoms):
    numberOfCoins = [float('inf')] * (n + 1)
    numberOfCoins[0] = 0

    for denom in denoms:
        for amount in range(len(numberOfCoins)):
            if denom <= amount:
                numberOfCoins[amount] = min(numberOfCoins[amount], numberOfCoins[amount - denom] + 1)
    if numberOfCoins[n] == float("inf"):
        return -1
    else:
        return numberOfCoins[n] 
    
# 5. Number Of Ways To Traverse Graph
def numberOfWaysToTraverseGraph(width, height):
    if width == 1 or height == 1:
        return 1

    return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)

# 6. Kadanes Algorithm
def kadanesAlgorithm(array):
    border = array[0]
    maxSum = array[0]
    for i in range(1, len(array)):
        current = array[i]
        border = max(current, border + current)
        maxSum = max(maxSum, border)
    return maxSum

# 7. Single Cycle Check
# keep track of number of jumps and current index
# use modulo to calculate wrapping around
# break loop if:
# index is 0, value of current is 0, or jumps more than number of elements
# if number of jumps = number of elements, its valid
def hasSingleCycle(array):
    jumps = position = 0
    
    while True:
        position += array[position]
        position %= len(array)
        jumps += 1

        if position == 0 or array[position] == 0 or jumps > len(array):
            break
    return jumps == len(array)

# 8. Breadth First Search
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while queue:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array  
    
# 9. Merge Sort
def mergeSort(array):
    if len(array) <= 1:
        return array

    # split the array
    middle = len(array) // 2
    left = mergeSort(array[:middle])
    right = mergeSort(array[middle:])

    # merge them together
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # leftovers
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def getItems(values, items):
    sequence = []
    i = len(values) - 1
    j = len(values[0]) - 1

    while i > 0:
        if values[i][j] == values[i - 1][j]:
            i -= 1
        else:
            sequence.append(i - 1)
            j -= items[i - 1][1]
            i -= 1
        if j == 0:
            break
    return list(reversed(sequence))

# 10. Knapsack Problem
def knapsackProblem(items, capacity):
    values = [[0 for i in range(0, capacity + 1)] for j in range(0, len(items) + 1)]
    for i in range(1, len(items) + 1):
        currentWeight = items[i - 1][1]
        currentValue = items[i - 1][0]

        for j in range(0, capacity + 1):
            if currentWeight > j:
                values[i][j] = values[i - 1][j]
            else:
                values[i][j] = max(
                    values[i - 1][j],
                    values[i - 1][j - currentWeight] + currentValue
                )
    return [values[-1][-1], getItems(values, items)]

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()