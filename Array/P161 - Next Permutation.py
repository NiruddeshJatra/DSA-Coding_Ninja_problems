# Time Complexity: O(n), where n is the length of the permutation list.
# The while loops each run in O(n) time and the reversing of the sublist also takes O(n) time.

# Space Complexity: O(1), because we are using a constant amount of extra space.

# INTUITION:
# The problem is to find the next lexicographical permutation of the given list of numbers.
# If no such permutation exists, we should rearrange it to the lowest possible order (sorted in ascending order).

# ALGO:
# 1. Traverse the list from the end to find the first pair where the earlier element is smaller than the later element.
# 2. Once found, traverse from the end again to find the first element larger than the identified smaller element.
# 3. Swap these two elements.
# 4. Reverse the sequence from the element next to the initially identified smaller element to the end of the list.

def nextPermutation(permutation, n):
    # Step 1: Find the first decreasing element from the end
    i = n - 2
    while i >= 0 and permutation[i] >= permutation[i + 1]:
        i -= 1

    if i >= 0:  # If such an element was found
        # Step 2: Find the element just larger than the found element
        j = n - 1
        while permutation[j] <= permutation[i]:
            j -= 1

        # Step 3: Swap the elements
        permutation[i], permutation[j] = permutation[j], permutation[i]

    # Step 4: Reverse the elements from i+1 to the end
    permutation[i + 1:] = reversed(permutation[i + 1:])
    return permutation
