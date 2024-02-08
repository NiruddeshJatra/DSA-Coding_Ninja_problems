# Time Complexity: O(n), where n is the length of the input list 'arr'.
# Space Complexity: O(n), where n is the number of unique elements in 'arr'.

# INTUITION:
# The code aims to find all elements that appear more than floor(n/3) times in the given list 'arr'.
# It uses the Counter class from the collections module to count the occurrences of each element.
# Then, it iterates through the counts dictionary and appends elements that satisfy the condition to the answer list.

# ALGORITHM:
# 1. Initialize an empty list 'ans' to store the elements that appear more than floor(n/3) times.
# 2. Count the occurrences of each element in the input list 'arr' using the Counter class.
# 3. Iterate through the counts dictionary:
#    - If the count of an element is greater than floor(n/3), append the element to 'ans'.
# 4. Return the list 'ans' containing the majority elements.

from collections import Counter

def majorityElementII(arr):
    counts = Counter(arr)
    ans = []
    for num, count in counts.items():
        if count > len(arr) // 3:
            ans.append(num)
    return ans

# Example usage:
arr = [3, 2, 3]
print(majorityElementII(arr))  # Output: [3]
