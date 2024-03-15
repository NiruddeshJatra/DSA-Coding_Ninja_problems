from collections import deque

def sumOfMaxAndMin(nums, n, k):
    # Time Complexity: O(n)
    # Space Complexity: O(k)

    # INTUITION:
    # This function calculates the sum of the maximum and minimum elements 
    # in each sliding window of size 'k' in the given list 'nums'. 
    # The approach involves maintaining two dequeues, 'maxq' and 'minq', 
    # to keep track of the maximum and minimum elements in the current window, 
    # respectively.

    # ALGO:
    # 1. Initialize variables: 'ans' to store the sum of maximum and minimum 
    #    elements in each window, 'maxq' and 'minq' as dequeues to store the 
    #    indices of maximum and minimum elements in the current window, and 
    #    'l' as the left pointer of the sliding window.
    # 2. Iterate through each index 'r' in the range of 'n', the length of 'nums'.
    #    2.1. While 'maxq' is not empty and the current element 'nums[r]' is greater 
    #         than the value at the index 'maxq[-1]' (rightmost element in 'maxq'), 
    #         pop elements from 'maxq' until 'nums[r]' is not greater than the value 
    #         at 'maxq[-1]'.
    #    2.2. Append the index 'r' to 'maxq'.
    #    2.3. Similar to step 2.1, update 'minq' with the current minimum elements.
    #    2.4. If the leftmost index 'l' is greater than the leftmost index in 'maxq' 
    #         or 'minq', pop the leftmost index from 'maxq' and 'minq' until 'l' is 
    #         not greater than the leftmost index in 'maxq' or 'minq'.
    #    2.5. If the current index 'r' has reached a position where the window size 
    #         is 'k', add the sum of the maximum and minimum elements from the 
    #         respective queues to 'ans'.
    #         - Increment 'l' to move the left pointer.
    # 3. Return 'ans'.

    ans = 0
    maxq, minq = deque(), deque()
    l = 0
    
    for r in range(n):
        while maxq and nums[r] > nums[maxq[-1]]:
            maxq.pop()
            
        maxq.append(r)
        
        while minq and nums[r] < nums[minq[-1]]:
            minq.pop()
        
        minq.append(r)
        
        if l > maxq[0]:
            maxq.popleft()
            
        if l > minq[0]:
            minq.popleft()
            
        if r >= k - 1:
            ans += nums[maxq[0]] + nums[minq[0]]
            l += 1
            
    return ans
