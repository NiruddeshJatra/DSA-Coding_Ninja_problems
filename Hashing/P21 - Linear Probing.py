# Time Complexity: O(n^2) - Worst case, all elements have the same hash, leading to linear search through the hash table
# Space Complexity: O(n) - Space required for the hash table

# ALGO
# 1. FIND the length of the array
# 2. CREATE a hash table of size 'n' initialized with -1
# 3. ITERATE through each key in the input array
#     a. CALCULATE the hash value of the key using modulo operation (%)
#     b. WHILE the hash table at position 'h' is not empty (-1)
#         i. INCREMENT 'h' by 1
#         ii. IF 'h' reaches the end of the hash table, reset 'h' to 0 (wrap around)
#     c. INSERT the key into the hash table at position 'h'
# 4. RETURN the hash table

def linearProbing(keys):
    n = len(keys)
    hashTable = [-1]*n
    for i in keys:
        h = i%n
        while hashTable[h] != -1:
            h += 1
            if h == n:
                h = 0
        hashTable[h] = i
    return hashTable
