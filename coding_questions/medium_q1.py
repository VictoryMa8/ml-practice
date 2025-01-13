'''
Medium Level Coding Questions (Part 1)

1. Smallest Difference

'''

# we are given two arrays, find the pair of two numbers that has the smallest absolute difference
def smallestDifference(arrayOne, arrayTwo):
    # initialize the 'smallest' value to record the best pair
    # the return value is a list named 'closest' that contains the pair
    smallest = float("inf")
    closest = []
    # look at each item in arrayOne
    for i in arrayOne:
        # for each item in arrayOne, look at each item in arrayTwo
        for j in arrayTwo:
            # compute their difference and get the absolute value of that, compare it to smallest
            if abs(i - j) < smallest:
                # if it is smaller than the current 'smallest', name it the new smallest difference
                smallest = abs(i - j)
                # update the list to return
                closest = [i, j]
    return closest

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()