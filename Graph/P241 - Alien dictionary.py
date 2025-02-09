# Time Complexity:
# - O(N * K), where:
#   N = number of words in dictionary
#   K = average length of each word
# - We need to examine each character of each word once
# - This problem requires building graph and topological sort for optimal solution

# Space Complexity:
# - O(26) = O(1) for adjacency list (max 26 lowercase letters)
# - O(26) = O(1) for visited set
# - O(26) = O(1) for result array
# - Overall space: O(1) since alphabet size is fixed

# INTUITION:
# In an alien dictionary, word order gives us clues about letter order.
# Think of English dictionary:
# "apple" comes before "banana" because 'a' comes before 'b'
# "cat" comes before "car" because 't' comes after 'r'
#
# By comparing adjacent words, we can:
# 1. Find first differing characters
# 2. These tell us relative ordering (like 'a' must come before 'b')
# 3. Build these relationships into a graph
# 4. Use topological sort to find valid alphabet order

# ALGORITHM:
# 1. Build graph from word pairs:
#    - Compare adjacent words character by character
#    - First differing characters give us an edge in our graph
# 2. Perform topological sort on resulting graph:
#    - Use DFS to find valid ordering
#    - Handle cycles (invalid dictionary case)
# 3. Return sorted characters as string

from collections import defaultdict, deque

def getAlienLanguage(dictionary: List[str], k: int) -> str:
   # Build adjacency list for character relationships
   adjacencyList = defaultdict(set)
   inDegree = defaultdict(int)
   
   # Initialize all possible characters
   allChars = set()
   for word in dictionary:
       allChars.update(list(word))
   
   # Compare adjacent words to build graph
   for i in range(len(dictionary) - 1):
       word1, word2 = dictionary[i], dictionary[i + 1]
       # Find first differing character
       for c1, c2 in zip(word1, word2):
           if c1 != c2:
               # If this ordering not already noted
               if c2 not in adjacencyList[c1]:
                   adjacencyList[c1].add(c2)
                   inDegree[c2] += 1
               break
               
   # Topological sort using Kahn's algorithm
   queue = deque([c for c in allChars if inDegree[c] == 0])
   result = []
   
   while queue:
       char = queue.popleft()
       result.append(char)
       
       for nextChar in adjacencyList[char]:
           inDegree[nextChar] -= 1
           if inDegree[nextChar] == 0:
               queue.append(nextChar)
   
   # Check if we found all characters (no cycles)
   if len(result) != len(allChars):
       return ""  # Invalid dictionary
       
   return ''.join(result)
