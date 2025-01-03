# Time Complexity:
# - O(N) where N is length of string
#   - One count operation: O(N)
#   - Two passes through string: O(N)

# Space Complexity:
# - O(1), using only boolean flags and counter

# INTUITION:
# String can be binary if # can be replaced to make sequence:
# - Either ascending (0 followed by 1s)
# - Or descending (1 followed by 0s)
# Check both possibilities with two passes
# Track # count to know when we have valid solution

# ALGO:
# 1. First pass (ascending check):
#    - Find first 0
#    - Count remaining # after 0
#    - Valid if all # used
# 2. Second pass (descending check):
#    - Find first 1
#    - Count remaining # after 1
#    - Valid if all # used
# 3. Return 1 if either check passes

def canItBeBinary(n: int, s: str) -> int:
   # Initialize flags and count #
   zeroFound = oneFound = False
   hashCount = s.count('#')
   
   # Check ascending possibility
   for c in s:
       if not zeroFound and c == '0':
           zeroFound = True
       if zeroFound and c == '#':
           hashCount -= 1
       if hashCount == 0:
           return 1
           
   # Check descending possibility
   for c in reversed(s):
       if not oneFound and c == '1':
           oneFound = True
       if oneFound and c == '#':
           hashCount -= 1
       if hashCount == 0:
           return 1
           
   return 0
