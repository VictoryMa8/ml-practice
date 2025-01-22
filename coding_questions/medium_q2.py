'''
Medium & Hard Level Coding Questions (Part 2)

1. Reverse Linked List
2. Quick Sort
3. Ways To Make Change (Infinite Supply)
4. Minimum Number Of Coins For Change

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

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()