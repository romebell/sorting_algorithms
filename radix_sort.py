# RADIX SORT
# Note: Input restricted to to positive integers
​
def radix_sort(ls):
    # Determine k (length of longest number)
    k = len(str(max(ls)))
    # Start a k loop
    print('this is k: ', k)
    for i in range(k):
        # Make buckets for values 0-9
        buckets = make_buckets()
        # Make inner n loop
        for j in range(len(ls)):
            # Determine the "place" we're looking at
            place = 10**i
            # Chop down the number to the correct digit
            digit = ls[j] // place
            # Get the bucket number
            bucket_num = digit % 10
            # Place the value into the correct bucket
            buckets[bucket_num].append(ls[j])
        # Mash the buckets together
        ls = flatten(buckets)
    return ls
​
def flatten(buckets):
    flat = []
    for bucket in buckets:
        flat += bucket
        print(flat)
    return flat 
​
def make_buckets():
    buckets = []
    for i in range(10):
        buckets.append([])
​
    return buckets
​
    
​
# TEST DATA 
test = [7, 3, 17, 37, 127, 333, 108, 999, 49, 521, 960, 187, 11, 16, 24, 48, 72, 360, 44, 676, 13, 42, 99, 101, 808, 206, 21, 22, 42, 10]
print('Sorted list: ', radix_sort(test))
# # Buckets:
# 0: [960, 360, 10]
# 1: [521, 11, 101, 21]
# 2: [72, 42, 22, 42]
# 3: [3, 333, 13]
# 4: [24, 44]
# 5: [555, 15]
# 6: [16, 676, 206]
# 7: [7, 17, 37, 127, 187]
# 8: [108, 48, 808]
# 9: [999, 49, 99]
