'''
Medium & Hard Level Coding Questions (Part 2)

1. Reverse Linked List

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

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()