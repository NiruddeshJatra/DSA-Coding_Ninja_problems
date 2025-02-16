# Time Complexity:
# - O(maxK * n) where maxK is maximum value of k and n is length of string
# - Each character can be decoded multiple times based on nested multiplications

# Space Complexity:
# - O(n) for the stack storing intermediate results
# - Additional O(n) for storing decoded substrings

# INTUITION:
# Process string character by character:
# - Letters go directly to result
# - Numbers & brackets need special handling for repetition
# Example: "3[a]2[bc]" breaks down as:
# 1. First "3[a]": Store 3 and "a", then repeat "a" 3 times
# 2. Then "2[bc]": Store 2 and "bc", then repeat "bc" 2 times
# Key insight: Stack helps handle nested encoded strings

# ALGO:
# 1. Process string character by character:
#    - If letter: add to result
#    - If number: collect full number
#    - If '[': push number and empty string
#    - If letter after '[': collect full string
#    - If ']': pop string and number, multiply and add to prior string
# 2. Return final decoded string

def decodeString(encodedString: str) -> str:
   decodedResult = ""
   currentIndex = 0
   stack = []  # Stores (number, partial_string) pairs
   
   while currentIndex < len(encodedString):
       currentChar = encodedString[currentIndex]
       
       # Case 1: Regular letter - add to result
       if currentChar.isalpha():
           decodedResult += currentChar
           currentIndex += 1
           continue
       
       # Case 2: Start of encoded section
       while currentChar != ']':
           # Collect number
           multiplier = ""
           while encodedString[currentIndex].isdigit():
               multiplier += encodedString[currentIndex]
               currentIndex += 1
           stack.append(multiplier)
           
           # Skip '['
           currentIndex += 1
           
           # Collect string until ']'
           currentString = ""
           while encodedString[currentIndex].isalpha():
               currentString += encodedString[currentIndex]
               currentIndex += 1
           stack.append(currentString)
           
           currentChar = encodedString[currentIndex]
       
       # Case 3: End of encoded section
       currentString = stack.pop()  # Get string to repeat
       multiplier = stack.pop()     # Get number of repetitions
       decodedSection = currentString * int(multiplier)
       
       # Either add to previous partial result or main result
       if stack:
           previousString = stack.pop()
           stack.append(previousString + decodedSection)
       else:
           decodedResult += decodedSection
           
       currentIndex += 1
   
   return decodedResult
