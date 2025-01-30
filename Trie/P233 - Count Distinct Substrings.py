# Time Complexity:
# - O(N²), where N is length of string s
# - Need to check all possible substrings
# - For each starting position i, we process up to N-i characters

# Space Complexity:
# - O(N²) in worst case for storing all distinct substrings in trie
# - Each node stores map of characters to child nodes

# INTUITION:
# Use trie to efficiently store and count distinct substrings.
# For each starting position, add all possible substrings to trie.
# Each new path in trie represents a unique substring.
# Add 1 to final count for empty string.

# ALGO:
# 1. Initialize trie root and counter
# 2. For each starting position i:
#    - Start at root node
#    - Add characters j from i to end:
#      - If char not in current node's map:
#        - Create new node and increment counter
#      - Move to next node
# 3. Return count + 1 (include empty string)

class Node:
   def __init__(self):
       self.letter = {}  # Maps chars to child nodes

def countDistinctSubstrings(s: str) -> int:
   trieRoot = Node()
   distinctCount = 0
   
   # Process all possible substrings
   for startPos in range(len(s)):
       currentNode = trieRoot
       
       # Add all substrings starting at startPos
       for endPos in range(startPos, len(s)):
           currentChar = s[endPos]
           
           # New substring found
           if currentChar not in currentNode.letter:
               currentNode.letter[currentChar] = Node()
               distinctCount += 1
               
           currentNode = currentNode.letter[currentChar]
   
   # Add 1 for empty string
   return distinctCount + 1
