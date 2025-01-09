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

def main():
    print("Hello")

if __name__ == "__main__":
    main()