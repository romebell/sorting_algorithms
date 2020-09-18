from random import shuffle
tries = 0
​
def is_sorted(ls):
    # Loop through the list
    # Make sure each item is less than (or equal) to the next
    for i in range(len(ls) - 1):
        if ls[i] > ls[i + 1]: return False
    return True
​
def bogo_sort(ls):
    global tries
    tries += 1
    # check if already sorted
    if is_sorted(ls): return ls
    # if not, shuffle list + check again!
    shuffle(ls)
    return bogo_sort(ls)
​
test = [1, 9, 23, 5, 2, 6, 45]
print('Testing', test, 'and it is ', bogo_sort(test), ' Sort was found after ', tries, ' tries')