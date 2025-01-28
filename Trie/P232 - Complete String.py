# Time Complexity:
# - O(N * L), where N is number of strings and L is max string length
# - Building trie: O(N * L)
# - Checking each string: O(N * L)

# Space Complexity:
# - O(N * L) for storing all strings in trie
# - Each node can have up to 26 children (lowercase English letters)

# INTUITION:
# Use trie to check if all prefixes of each string exist as complete words.
# For each string, verify that every prefix node marks end of a word.
# Among valid strings, return longest one or lexicographically smaller if tied.

# ALGO:
# Trie Insert:
# 1. Build trie node by node for each character
# 2. Mark last node as word end

# isPrefix: 
# 1. Check if each prefix exists in trie
# 2. Verify each node in path is word end
# 3. Return false if any prefix invalid

# completeString:
# 1. Build trie from all strings
# 2. Check each string if all its prefixes exist
# 3. Track longest valid string
# 4. If tie, keep lexicographically smaller

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

   def isPrefix(self, prefix: str) -> bool:
       currentNode = self.root
       for char in prefix:
           if char in currentNode.children:
               currentNode = currentNode.children[char]
               if not currentNode.isEndNode:
                   return False
           else:
               return False
       return True

def completeString(n: int, strs: List[str]) -> str:
   if not strs:
       return None
       
   # Build trie
   trie = Trie()
   for word in strs:
       trie.insert(word)
       
   # Find longest valid string
   longestString = ''
   for word in strs:
       if trie.isPrefix(word):
           if len(word) > len(longestString):
               longestString = word
           elif len(word) == len(longestString) and word < longestString:
               longestString = word
               
   return longestString if longestString else None
