def findPages(arr: [int], n: int, m: int) -> int:
    def isPossible(pages):
        cntStudent, curPage = 1, 0
        for i in range(n):
            if curPage + arr[i] <= pages:
                curPage += arr[i]
            else:
                cntStudent += 1
                curPage = arr[i]
            if cntStudent > m:
                return False
        return True
    
    if n < m:
        return -1
    l, r = max(arr), sum(arr)
    while l <= r:
        pages = (l + r) // 2
        if isPossible(pages):
            r = pages - 1
        else:
            l = pages + 1
    return l

# Time Complexity: O(n log(sum - max))
# Space Complexity: O(1)

# INTUITION:
# The problem is to allocate books to 'm' students such that the maximum number of pages assigned to a student is minimized.
# To solve this, we use binary search to determine the minimum possible maximum pages that can be assigned to a student.
# We iterate through possible maximum pages and use a helper function 'isPossible' to check if it's feasible to allocate books within the given constraints.

# ALGO:
# 1. Define a helper function 'isPossible' to check if a given number of pages can be allocated to 'm' students.
#    - Initialize count of students and current page count.
#    - Iterate through the array and allocate pages to the current student until the limit is reached.
#    - If the limit is exceeded, allocate to a new student and increment the student count.
#    - If the student count exceeds 'm', return False.
# 2. If the number of books is less than the number of students, return -1.
# 3. Initialize the binary search bounds:
#    - 'l' as the maximum number of pages in a single book (minimum possible maximum pages).
#    - 'r' as the sum of all pages (maximum possible maximum pages).
# 4. Perform binary search:
#    - Calculate the middle value of pages.
#    - Use 'isPossible' to check if the middle value is a feasible allocation.
#    - If feasible, move the right bound to mid-1 to find a smaller possible maximum.
#    - If not feasible, move the left bound to mid+1 to find a larger possible maximum.
# 5. Return the left bound as the minimum possible maximum pages.
