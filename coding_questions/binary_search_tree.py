''' 
Binary Search Tree Functionality

1. Implement BST
2. Validate BST
3. In Order, Pre-Order, & Post-Order Traversal
4. Minimum Height Construction BST
5. Find Kth Largest Value In BST
6. Reconstruct BST
7. Invert Binary Tree

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

# 5. Find Kth Largest Value In BST
def findKthLargestValueInBst(tree, k):
    count = 0
    stack = []
    curr = tree

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.right
        else:
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.value
                
            curr = curr.left

# 6. Reconstruct BST
def reconstructBst(preOrderTraversalValues):
    root = BST(preOrderTraversalValues[0])
    for i in range (1, len(preOrderTraversalValues)):
        root.insert(preOrderTraversalValues[i])
    return root

# 7. Invert Binary Tree
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        current.left, current.right = current.right, current.left
        queue.append(current.left)
        queue.append(current.right)

# 8. Find Successor
# a node's successor is the next node to be visited when traversing using in-order traversal method
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def leftmostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode

def rightmostParent(node):
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    return currentNode.parent

def findSuccessor(tree, node):
    if node.right is not None:
        return leftmostChild(node.right)
    return rightmostParent(node)

def main():
    array1 = [5, 10, 3, 2, 8, 7, 4]
    minHeightBst(array1)
    

if __name__ == "__main__":
    main()