# we have a linked list sorted in ascending order
# remove all duplicates from it
# we just go through the linked list see compare the current node to the next node
# since its sorted, we can go node by node and check to see if they're equal
# if they are, just make the current node point to the next next node
def removeDuplicatesFromLinkedList(linkedList):
    # important to note that the linked list is sorted
    # initialize head node
    curr = linkedList
    # while we're not at the end
    while curr.next is not None:
        # if current node's value is equal to the next value
        if curr.value == curr.next.value:
            # make current node point to the next node
            curr.next = curr.next.next
        else:
            # otherwise, just go to the next node
            curr = curr.next
    return linkedList

# find the middle node, if the length if even, get the 'middle-right' node
# fast traveses the linked list 'twice as fast', so by the time the while loop is done iterating,
# the slow one is at the middle point
# make sure the condition still goes if fast.next is not None
# that way we reach the end even if we go past the end 
def middleNode(linkedList):
    # set up two things to traverse the linked list
    slow = linkedList
    fast = linkedList

    while fast and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow

# fibonacci sequence
# we have our starting numbers
# iterate until n - 1 exclusive
# we store lastlast number in temp, last number in x and next number in y
def getNthFib(n):
    # first numbers of the sequence are 0, 1
    # the nth number is the sum of the (n - 1)th and (n - 2)th numbers
    # so the 2nd number is 0 + 1 = 1, 3rd is 1 + 1 = 2
    x = 0
    y = 1
    # n - 2, n - 1, and n
    for i in range(n - 1):
        temp = x # 0 1 1 2 3
        x = y # 1 1 2 3 5
        y += temp # 1 2 3 5 8

    return x

def main():
    print("Hello")

if __name__ == "__main__":
    main()