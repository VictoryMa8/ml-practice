'''
Easy Level Coding Questions (Part 1)

1. Depth First Search
2. Two Number Sum
3. Is Valid Subsequence
4. Sorted Squared Array
5. Tournament Winner
6. Transpose Matrix
7. Find Closest Value In BST
8. Branch Sums
9. Node Depths
10. Minimum Waiting Time
11. Class Photos
12. Tandem Bicycle
13. Optimal Freelancing **
14. Evaluate Expression Tree **

'''


# this is a tree class
class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # simple depth first search (go down as far as we can on the tree before we go back up)
    # visit every node in the tree
    # we use a stack to achieve this
    def depthFirstSearch(self, array):
        # create stack, add root node
        to_visit = [self]
        # while stuff is still in to_visit
        while len(to_visit) > 0:
            # take an element out of to_visit, name it curr, and
            # add it to array
            curr = to_visit.pop()
            array.append(curr.name)
            # iterate through all children, add them to to_visit
            # also children needs to be reversed
            # (that way we go left to right)
            for i in curr.children[::-1]:
                to_visit.append(i)
        return array

# go through an array, if we are able to find two numbers that reach the target, return them in a list
# for time complexity sake, use a set to record all numbers in the list
# then, iterate through the list, make note of (target - currentNumber)
# if this number is seen in the set, then we have two numbers that we can add to reach target
# also make sure that it's not just the same number twice
def twoNumberSum(array, targetSum):
    # make a set out of the array O(n)
    mySet = set(array)
    # traverse the array O(n)
    for i in array:
        # record targetSum minus current value in traversal
        diff = targetSum - i # O(1)
        # if this difference is in mySet, we can reach targetSum
        # also the two nums can't be the same num
        if diff in mySet and diff is not i:
            return [i, diff] # O(1)
    # if can't reach targetSum, return empty array
    return []

# go through an array to find a valid 'subsequence'
# we are given a larger array, and a smaller array called sequence
# if we can find sequence in the same exact order in the larger array, it's valid
# for example, [1, 2, 3, 4, 5] and [1, 5]
# 1 and 5 are in the same order they appear in the larger array, so its valid
# iterate through larger array, and only push through sequence if we see the next element
# see if we reach the end, if yes, then True
def isValidSubsequence(array, sequence):
    # track how far we've gone in sequence
    trackSeq = 0
    # traverse through array
    for i in array:
        # only keep going if we need to look for more items from seqeuence
        if trackSeq < len(sequence):
            # if the current value in sequence, look at next item in sequence
            if i == sequence[trackSeq]:
                trackSeq += 1
    # if we got to the last item in sequence, then
    # trackSeq would equal last index + 1 (or length of the sequence)
    if trackSeq == len(sequence):
        return True
    # if we didn't find all items, return false
    else:
        return False
    
# make a list that contains the squared elements of the original list
def sortedSquaredArray(array):
    # create copy of array
    copy = array
    # traverse copy
    for i in range(len(copy)):
        # self explanatory
        copy[i] = copy[i] * copy[i]
    copy.sort()
    return copy

# there is a list of 'games played', that contains lists of 2 elements (the two teams) - team[0] is home, team[1] away
# results is a list of the outcome, where results[0] shows the result of competitions[0]
# if it is 1, the home team won, 0 the away team won
# using a dictionary to keep track of teams with points, we iterate through each list to find the tournament winner
def tournamentWinner(competitions, results):
    myDict = {} # create dict of teams
    maxPoints = 0
    tourneyResult = ""
    for i in range(len(competitions)): # traverse through games
        homeTeam = competitions[i][0] # initialize home team
        awayTeam = competitions[i][1] # away team
        winner = homeTeam if results[i] == 1 else awayTeam
        if winner in myDict:
            myDict[winner] += 3
        else:
            myDict[winner] = 3
    for i in myDict:
        if myDict[i] > maxPoints:
            maxPoints = myDict[i]
            tourneyResult = i
    return tourneyResult

# we are trying to flip a matrix, so the original number of rows becomes the number of columns
# and the original number of columns becomes the number of rows
# we create a list of lists of length m, the number of original rows
# and height n, the number of original columns
def transposeMatrix(matrix):
    # the number of rows becomes the number of columns of copy
    m = len(matrix) 
    n = len(matrix[0])
    # some crazy python stuff here
    # with [0] * m, we create a list of length m (rows), filled with 0
    # then we do that n times with the for loop (columns)
    # what the heck
    copy = [[0] * m for i in range(n)]
    for i in range(m):
        for j in range(n):
            copy[j][i] = matrix[i][j]    
    return copy

# we are trying to find the closest value to target in the tree
# we first make the root node the temporary 'closest' to target
# we go through the tree to check if the current node is closer than 'closest'
# if not, then if current is > than target, we know that everything to the right is also > in difference
# so we check the left, or vice versa
def findClosestValueInBst(tree, target):
    # tree is the current node
    closest = tree.value # we just have the root node as closest for now
    while tree is not None: # while we're not looking at null
        if closest == target: # if root == target
            break;
        # if current node is closer to target, closest = current
        elif abs(target - tree.value) < abs(target - closest):
            closest = tree.value
        # otherwise, if current is greater than target,
        # we know to only look at the left side,
        # because the nodes to the right of current
        # are all greater in value, meaning greater in difference
        elif tree.value > target:
            tree = tree.left
        else:
        # if current < target
            tree = tree.right
    return closest

# we are trying to get the sum of all 'branches'
# a branch is the path to any leaf node
# we go through all possible 'paths', adding the value of each node together
def branchSums(root):
    # if tree is empty
    if root is None:
        return []
    # recursive calls
    left = branchSums(root.left)
    right = branchSums(root.right)
    branch = left + right
    if branch:
        return [i + root.value for i in branch]
    else:
        return [root.value]

# we are trying to find 'depth' (how far down) each node is, and sum it all up
# for example, the root node has a depth of 0, and its children have depths of 1
# if we have a small tree with a root node and two leaf nodes, we have a total of 2
def nodeDepths(root):
    # using DFS to traverse through the tree
    # create stack, add root node
    stack = [root]
    # create list with the sum depth at each level
    nodeDepthSum = [0]
    result = 0
    # while stuff is still in stack
    while len(stack) > 0:
        curr = stack.pop()
        currRowSum = nodeDepthSum.pop()
        # add current row's depth sum to result
        result += currRowSum
        # if there is a node to the right, put it in the stack
        if curr.right is not None:
            stack.append(curr.right)
            nodeDepthSum.append(currRowSum + 1)
        # same with left
        if curr.left is not None:
            stack.append(curr.left)
            nodeDepthSum.append(currRowSum + 1)        
    return result

# we are given a list of queries, with the execution time of items
# the wait time is determined by the execution time of the previous items, find the minimum total wait time
# for example queries = [5, 6, 7, 8], queries[1] has a wait time of 5, queries[2] has a wait time of 11
def minimumWaitingTime(queries):
    # order the array to maximize efficiency
    # now the longest wait time is at the end
    queries.sort()
    # initalize a total for wait times
    total = 0
    # initialize a wait time to assign each query
    wait = 0
    for i in range(len(queries)):
        # first query has a wait time of 0
        if i > 0:
            # the wait time for a query is the total value of all prev queries
            wait += queries[i-1]
            # after figuring that out for each item, add it to the total
            total += wait
    return total

# there are two lists to represent the rows of students
# every student of the same color is in one row, the list contains the heights of these students
# see if we are able to get a picture of all students so that a student in the front isn't blocking anyone
def classPhotos(redShirtHeights, blueShirtHeights):
    # sort rows to ensure tallest is behind tallest of each row
    redShirtHeights.sort()
    blueShirtHeights.sort()
    # for now we assume that its possible that any student in the front
    # is shorter than the person behind them
    blueFront = True
    redFront = True
    # we just dont know which row is in the front, so we iterate
    for i in range(len(redShirtHeights)):
        # if at any point a red shirt is taller than a blue shirt,
        # we flag a red front as impossible
        if redShirtHeights[i] >= blueShirtHeights[i]:
            redFront = False
        # same goes for a blue front
        if blueShirtHeights[i] >= redShirtHeights[i]:
            blueFront = False
    # if we can achieve any front, we have a valid group of students
    if redFront or blueFront:
        return True
    return False

# a tandem bike has two pedalers, the fastest pedaler determines the overall speed of the bike
# pair the cyclers so that we get either the fastest possible speed or slowest possible speed
# we sort the cyclers, if we want fastest speed, we pair the slow ones with the fastest ones
# if we want the slowest, we pair the slowest with the slowest
# that way if we avoid something like (1, 10) = 10, 9 extra speed compared to if we couldve done (1,1) = 1
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # sort both lists
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    # if we want the fastest, we should pair the slowest with the fastest
    # that way the bicycle achieves max speed
    if fastest:
        blueShirtSpeeds.reverse()
    # if we want the slowest, we pair the slowest with the slowest
    maxSpeed = 0
    for i in range(len(redShirtSpeeds)):
        maxSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return maxSpeed

# will write more detailed explanation later
def optimalFreelancing(jobs):
    # if no jobs, return 0
    if len(jobs) == 0:
        return 0
    # track max profit
    maxProfit = 0
    # start from day 7
    numberOfDays = 7
    # iterate through the week, starting at day 7
    while numberOfDays > 0:
        # initialize best pay for the current day
        currentDayMaxPayment = 0
        # record the index of the job
        indexToRemove = None
        # iterate through jobs
        for i, job in enumerate(jobs):
            # if a job's deadline is greater than or equal to current day
            if job["deadline"] >= numberOfDays:
                # if the payment is better than current max for the day
                if job["payment"] > currentDayMaxPayment:
                    # make it the max
                    currentDayMaxPayment = job["payment"]
                    # record its index
                    indexToRemove = i
        # remove the item at index
        # add to the max profit achievable 
        if indexToRemove is not None:
            jobs.pop(indexToRemove)
            maxProfit += currentDayMaxPayment
        # go to the next day
        numberOfDays -= 1
    return maxProfit

# explaining ltr **
def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value
        
    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftValue + rightValue
    if tree.value == -2:
        return leftValue - rightValue
    if tree.value == -3:
        return int(leftValue / rightValue)
        
    return leftValue * rightValue

def main():
    print("Hello")

if __name__ == "__main__":
    main()