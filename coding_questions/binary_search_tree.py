''' 
Binary Search Tree Functionality

1. Implementation
2. Validation
3. Traversal
4. Minimum Height Construction

'''

# 1. Implementation
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def getMinimumValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMinimumValue()
            
def insert(self, value):
    if value < self.value:
        if self.left is None:
            self.left = BST(value)
        else:
            self.left.insert(value)

    elif value >= self.value:
        if self.right is None:
            self.right = BST(value)
        else:
            self.right.insert(value)
        
    return self

def contains(self, value):
    if value < self.value:
        if self.left is None:
            return False
        else:
            return self.left.contains(value)
                
    elif value > self.value:
        if self.right is None:
            return False
        else:
            return self.right.contains(value)
    elif value == self.value:
        return True

def remove(self, value, parent = None):
    if value < self.value:
        if self.left is not None:
            self.left.remove(value, self)

    elif value > self.value:
        if self.right is not None:
            self.right.remove(value, self)
                
    elif value == self.value:
        if self.left is not None and self.right is not None:
            self.value = self.right.getMinimumValue()
            self.right.remove(self.value, self)

        elif parent is None:
            if self.left is not None:
                self.value = self.left.value
                self.right = self.left.right
                self.left = self.left.left

            elif self.right is not None:
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right

        elif parent.left == self:
            if self.left is not None:
                parent.left = self.left
            else:
                parent.left = self.right

        elif parent.right ==self:
            if self.left is not None:
                parent.right = self.left
            else:
                parent.right = self.right
    return self

# 2. Validation
def validateBst(tree, min = float('-inf'), max = float('inf')):
    if tree == None:
        return True
    elif tree.value < min or tree.value >= max:
        return False

    return validateBst(tree.left, min, tree.value) and validateBst(tree.right, tree.value, max)

# 3. Traversal
def inOrderTraverse(tree, array):
    stack = []
    if tree is not None:
        curr = tree
    while stack or curr is not None:
        while curr is not None:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        array.append(curr.value)
        curr = curr.right
    return array
    pass


def preOrderTraverse(tree, array):
    stack = []
    if tree is not None:
        stack.append(tree)
    while stack:
        curr = stack.pop()
        array.append(curr.value)
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    return array
    pass

def postOrderTraverse(tree, array):
    stack = []
    if tree is not None:
        stack.append(tree)
    while stack:
        curr = stack.pop()
        array.append(curr.value)
        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)
    return array[::-1]

# 4. Minimum Height Contruction
def minHeightBst(array):
    left = 0
    right = len(array) - 1
    middle = (left + right) // 2
    if left > right:
        return
    currentNode = BST(array[middle])
    currentNode.left = minHeightBst(array[:middle])
    currentNode.right = minHeightBst(array[middle + 1:])
    return currentNode