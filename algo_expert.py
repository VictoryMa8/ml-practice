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
    
def sortedSquaredArray(array):
    # create copy of array
    copy = array
    # traverse copy
    for i in range(len(copy)):
        # self explanatory
        copy[i] = copy[i] * copy[i]
    copy.sort()
    return copy

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
    


def main():
    print("Hello")

if __name__ == "__main__":
    main()