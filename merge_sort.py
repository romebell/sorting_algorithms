# MERGE SORT - best/average O(n*log(n)): worst - O(n^2)
# BASE CASE: 1 or fewer items is considered sorted!
# RECURSIVE CASE: Any other length
# nums = [3, 78, 23, 466, 324, 2, 12, 546, 17, 56, 23, 123, 343, 87, 94, 45, 6, 9, 234, 36]

# # , num, left=0, right=0

# def merge_sort(ls):
#     # Base Case
#     if len(ls) <= 1:
#         return ls

#     # Recursive Step
#     # Find a midpoint of the list
#     half = round(len(ls) / 2)

#     # Divide the list in half
#     left = ls[0:half]
#     right = ls[half:]

#     print(left)
#     print(right)

#     # Sort each side
#     left_sorted = merge_sort(left)
#     right_sorted = merge_sort(right)

#     # Merge the two list back together
#     return merge(left_sorted, right_sorted)

# merge_sort(nums)

# def merge(ls1, ls2):
#     print('ls1', ls1) # 
#     print('ls2', ls2) # [546, 17, 56]
#     sorted_list = [] # 2, 3, 12, 78, 23, 466, 324
#     # Running a while loop until both list are empty
#     while len(ls1) and len(ls2):
#         if ls1[0] > ls2[0]:
#             sorted_list.append(ls2.pop(0))
#         else:
#             sorted_list.append(ls1.pop(0))
#     sorted_list = sorted_list + ls1 + ls2
#     print('sorted_list', sorted_list)
#     return sorted_list  








    


# MERGE SORT - best/average O(n*log(n)): worst - O(n^2)
# BASE CASE: 1 or fewer items is considered sorted!
# RECURSIVE CASE: Any other length
nums = [3, 78, 23, 466, 324, 2, 12, 546, 17, 56, 23, 123, 343, 87, 94, 45, 6, 9, 234, 36]
def merge_sort(ls):
    # Base Case
    if len(ls) <= 1:
        return ls
    # Recursive Case
    # 1. Find the midpoint of the list
    mid = len(ls) // 2 # // is for integer division
    # 2. Divide the list in half
    left = ls[:mid] # :mid is shorthand for 0:mid
    print('left list: ', left)
    right = ls[mid:] # mid: is shorthand for mid - end of the list
    print('right list: ', right)
    # 3. Sort each side
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    # 4. Merge the two lists back together
    return merge(left_sorted, right_sorted)
# O(n) - combines two sorted lists into one sorted list
def merge(ls1, ls2):
    print('ls1: ', ls1)
    print('ls2: ', ls2)
    sort = []
    while len(ls1) and len(ls2):
        if ls1[0] > ls2[0]:
            sort.append(ls2.pop(0))
        else:
            sort.append(ls1.pop(0))
    sort = sort + ls1 + ls2
    print('Sorted List: ', sort)
    return (sort)
merge_sort(nums)