# Time Complexity:
# - Insert: O(L), where L is length of word
# - CountWordsEqualTo: O(L)
# - CountWordsStartingWith: O(L) 
# - Erase: O(L)
# All operations involve traversing word characters once

# Space Complexity:
# - O(N * L) where N is total number of words and L is average word length
# - Each node stores children map and two counters
# - Erase uses O(L) stack space

# INTUITION:
# Enhanced Trie that maintains two counters per node:
# - endCount: number of words ending at this node
# - freq: number of words passing through this node
# This allows efficient counting of exact matches and prefixes.
# Deletion updates counters and removes unused nodes.

# ALGO:
# Insert:
# 1. Traverse word chars, create new nodes if needed
# 2. Increment freq for each node in path
# 3. Increment endCount for last node

# CountWordsEqualTo:
# 1. Traverse word to find last node
# 2. Return its endCount

# CountWordsStartingWith:
# 1. Traverse prefix to find last node
# 2. Return its freq

# Erase:
# 1. Check if word exists
# 2. Traverse word, decrement freq
# 3. Decrement endCount for last node
# 4. Clean up unused nodes

class TrieNode:
   def __init__(self):
       self.children = {}  # Maps chars to child nodes
       self.endCount = 0   # Count of words ending here
       self.freq = 0       # Count of words passing through

class Trie:
   def __init__(self):
       self.root = TrieNode()

   def insert(self, word: str) -> None:
       currentNode = self.root
       
       for char in word:
           if char not in currentNode.children:
               currentNode.children[char] = TrieNode()
           currentNode = currentNode.children[char]
           currentNode.freq += 1
           
       currentNode.endCount += 1

   def countWordsEqualTo(self, word: str) -> int:
       currentNode = self.root
       
       for char in word:
           if char in currentNode.children:
               currentNode = currentNode.children[char]
           else:
               return 0
               
       return currentNode.endCount

   def countWordsStartingWith(self, word: str) -> int:
       currentNode = self.root
       
       for char in word:
           if char in currentNode.children:
               currentNode = currentNode.children[char]
           else:
               return 0
               
       return currentNode.freq

   def erase(self, word: str) -> None:
       if self.countWordsEqualTo(word) == 0:
           return
           
       currentNode = self.root
       nodeStack = []
       
       # Traverse and update frequencies
       for char in word:
           nodeStack.append((currentNode, char))
           currentNode = currentNode.children[char]
           currentNode.freq -= 1
           
       # Update end count
       currentNode.endCount -= 1
       
       # Clean up unused nodes
       while nodeStack:
           parentNode, char = nodeStack.pop()
           childNode = parentNode.children[char]
           if childNode.freq == 0 and childNode.endCount == 0:
               del parentNode.children[char]
             
