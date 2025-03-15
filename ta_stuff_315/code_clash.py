from PythonFruits.Fruit import Fruit
from PythonFruits.Tomato import Tomato
from PythonFruits.Grape import Grape
from PythonFruits.Apple import Apple

from PythonChildren.Child import Child

# PROBLEM 1
def period(mylist):
    # if the list is empty, the period is 0
    if not mylist:
        return 0
    
    # length of the list
    n = len(mylist)
    
    # try every possible period length from 1 to n
    for period_length in range(1, n + 1):
        # Assume this is the period until proven otherwise
        is_period = True
        
        # check if the list repeats with this period length
        # by comparing each element with the element that is 'period_length' positions ahead
        for i in range(n - period_length):
            if mylist[i] != mylist[i + period_length]:
                # found a mismatch (this isn't the period)
                is_period = False
                break
        
        # if we didn't find any mismatches we found our period
        if is_period:
            return period_length
    
    # if no smaller period is found the period is the length of the list
    return n

# PROBLEM 2
def leastNumCoins(USD):
    # convert dollars and cents to total cents
    dollars = USD[0]
    cents = USD[1]
    total_cents = (dollars * 100) + cents 
    
    # initialize the result list for coins
    coins = [0, 0, 0, 0]
    
    # calculate quarters (25 each)
    coins[0] = total_cents // 25  # integer division to get number of quarters
    total_cents %= 25             # update remaining cents using modulo
    
    # calculate dimes (10 each)
    coins[1] = total_cents // 10
    total_cents %= 10
    
    coins[2] = total_cents // 5 
    total_cents %= 5 
    
    coins[3] = total_cents
    
    return coins

# PROBLEM 3
def validSmoothie(fruitList):
    # initialize vars to track weights
    total_weight = 0
    sweet_weight = 0
    sour_weight = 0
    
    # check each fruit in the list
    for fruit in fruitList:
        # get the weight of the current fruit
        weight = fruit.getWeight()
        total_weight += weight
        
        # check if any fruit is moldy
        if isinstance(fruit, Apple) and fruit.isMoldy():
            return False  # smoothie is inedible
        if isinstance(fruit, Tomato) and fruit.isMoldy():
            return False
        
        # calculate sweet and sour weights
        if isinstance(fruit, Apple):
            sweet_weight += weight
        elif isinstance(fruit, Grape):
            if fruit.isSour():
                sour_weight += weight
            else:
                sweet_weight += weight
        elif isinstance(fruit, Tomato):
            sour_weight += weight
    
    # calculate percentages
    sweet_percentage = sweet_weight / total_weight * 100
    sour_percentage = sour_weight / total_weight * 100
    
    # check if smoothie meets criteria (no more than 80% sweet and no more than 70% sour)
    return sweet_percentage <= 80 and sour_percentage <= 70

# PROBLEM 4
def badChildSorter(childList):    
    # sort children by height
    heights = []
    for child in childList:
        heights.append(child.getHeight())
    heights.sort()
    
    # Check which children are in the correct position
    for i in range(len(childList)):
        child = childList[i]
        
        # If the child's height matches the sorted height at this position,
        # they are in the correct position
        if child.getHeight() == heights[i]:
            # They're at the right height - send to school
            child.setLocation("School")
        else:
            # Child is out of order - assign location based on behavior
            behavior = child.getBehavior()
            
            if behavior == "good":
                child.setLocation("Yard")
            elif behavior == "ok":
                child.setLocation("Principal")
            else:  # behavior == "bad"
                child.setLocation("Home")

    # get all children assigned to school
    school_children = []
    for child in childList:
        if child.getLocation() == "School":
            school_children.append(child)

    for i in range(len(school_children) - 1):
        if school_children[i].getHeight() > school_children[i+1].getHeight():
            # if any child is taller than the next one, they are out of order
            # move them based on behavior
            behavior = school_children[i].getBehavior()
            if behavior == "good":
                school_children[i].setLocation("Yard")
            elif behavior == "ok":
                school_children[i].setLocation("Principal")
            else:
                school_children[i].setLocation("Home")

# PROBLEM 5
def noMoreSad(sadness, money):
    # calculate max treats we can buy
    max_treats = money / 0.10
    
    # calculate treats needed to reduce as much sadness as possible
    treats_needed = min(max_treats, (sadness + 1) // 2)
    
    # calculate money spent on treats
    money_spent = treats_needed * 0.10
    
    # calculate remaining sadness after treats
    remaining_sadness = sadness - (treats_needed * 2)
    
    # calculate pet time needed
    minutes_spent = 0
    if remaining_sadness > 0:
        minutes_spent = (remaining_sadness + 3) // 4 * 5
    
    # print the result
    if minutes_spent > 0:
        print(f"Spent {money_spent} Dollars and {minutes_spent} Minutes to Cheer Up the Salamander.")
    else:
        print(f"Spent {money_spent} Dollars to Cheer Up the Salamander.")

def main():
    # PROBLEM 1
    test_list1 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    test_list1 = [1, 2, 3, 4, 1, 2, 3, 4, 1, 7]
    print(period(test_list1))

    # PROBLEM 2
    test_coins1 = [2, 39]
    print(leastNumCoins(test_coins1))

    # PROBLEM 3
    fruits1 = [Grape(30, s = True), Tomato(70, m = False)]
    fruits2 = [Apple(30, m = True), Grape(70, s = True)]
    print(validSmoothie(fruits1))
    print(validSmoothie(fruits2))

    # PROBLEM 4
    child1 = Child(120, "good")
    child2 = Child(130, "ok")
    child3 = Child(140, "bad")
    children1 = [child1, child2, child3]
    for i in children1:
        print(i.getLocation())
    badChildSorter(children1)
    for i in children1:
        print(i.getLocation())

    child4 = Child(150, "good")
    child5 = Child(125, "ok")
    child6 = Child(135, "bad")
    children2 = [child6, child4, child5]
    for i in children2:
        print(i.getLocation())
    badChildSorter(children2)
    for i in children2:
        print(i.getLocation())

    # PROBLEM 5
    sad1 = 1000
    money1 = 45
    noMoreSad(sad1, money1)

if __name__ == "__main__":
    main()
