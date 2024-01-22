# Time Complexity: O(n)
# Space Complexity: O(n)


from collections import Counter

def minimumOperation(arr, n):
    freqDict = Counter(arr)
    mostFreq = max(freqDict.values())
    return n-mostFreq
