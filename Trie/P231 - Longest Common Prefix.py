# Time Complexity:
# - O(N * L), where N is number of strings and L is length of shortest string
# - Building trie takes O(N * L)
# - Finding common prefix takes O(L)

# Space Complexity:
# - O(N * L) for storing all strings in trie
# - Each node can have up to 26 children (lowercase English letters)

# INTUITION:
# Use a trie to efficiently identify common prefix.
# If at any point we have multiple branches or word end,
# we've found longest common prefix since it diverges after.
# Single path in trie represents common prefix.

# ALGO:
# 1. Build trie from all strings
# 2. Start from root and traverse down
# 3. Stop when either:
#    - Node has multiple children (strings diverge)
#    - Node marks end of word (shortest string ends)
# 4. Build prefix by collecting chars along path

class TrieNode:
   def __init__(self):
       self.children = {}
       self.isEndNode = False

class Trie:
   def __init__(self):
       self.root = TrieNode()
       
   def insert(self, word: str) -> None:
       currentNode = self.root
       
       for char in word:
           if char not in currentNode.children:
               currentNode.children[char] = TrieNode()
           currentNode = currentNode.children[char]
           
       currentNode.isEndNode = True

def longestCommonPrefix(strs, n):
   if not strs:
       return ''
       
   # Build trie from strings
   trie = Trie()
   for word in strs:
       trie.insert(word)
       
   # Find longest common prefix
   currentNode = trie.root
   commonPrefix = ''
   
   while currentNode:
       # Stop if multiple branches or word end
       if len(currentNode.children) > 1 or currentNode.isEndNode:
           return commonPrefix
           
       # Get only child's character
       currentChar = list(currentNode.children)[0]
       commonPrefix += currentChar
       
       # Move to next node
       currentNode = currentNode.children[currentChar]
       
   return commonPrefix
