# Time Complexity:
# - O(N) where N is length of string
#   - Single pass through string

# Space Complexity:
# - O(1), only using counter variable

# INTUITION:
# String is valid if it changes character at most once:
# - Track character transitions
# - If we see more than one change, invalid
# - Example: "000111" valid, "010" invalid

# ALGO:
# 1. Track character transitions (repeat)
# 2. For each character after first:
#    - If different from previous, increment repeat
#    - If repeat reaches 2, return 0 (invalid)
# 3. Return 1 (valid) if we finish loop

def splitString(n: int, s: str) -> int:
   repeat = 0
   
   # Check character transitions
   for i in range(1, len(s)):
       if s[i] != s[i-1]:
           repeat += 1
       if repeat == 2:
           return 0
           
   return 1
