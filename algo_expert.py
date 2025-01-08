class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

def main():
    print("Hello")

if __name__ == "__main__":
    main()