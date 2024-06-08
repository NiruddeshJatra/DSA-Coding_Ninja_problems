    # Time Complexity: O(2^n), where n is the number of '?' characters in the input string.
    # Space Complexity: O(n * 2^n), for storing the permutations and recursive call stack.
    
    # INTUITION:
    # This problem can be approached using backtracking. The idea is to generate all possible
    # permutations of the input string by replacing each '?' with both '0' and '1'. This ensures
    # that we cover all possible binary strings that can be formed from the input string.
    
    # ALGO:
    # 1. Initialize `ans` to store all the binary string permutations and `temp` to store the current permutation.
    # 2. Define the recursive function `binaryPermutations(i)`:
    #     2.1 If `i` equals the length of the input string, join `temp` into a string and add it to `ans`, then return.
    #     2.2 If the character at position `i` in the input string is '?':
    #         2.2.1 Append '0' to `temp`, call `binaryPermutations(i+1)`, and then pop the last character from `temp`.
    #         2.2.2 Append '1' to `temp`, call `binaryPermutations(i+1)`, and then pop the last character from `temp`.
    #     2.3 If the character at position `i` is not '?':
    #         2.3.1 Append the character to `temp`, call `binaryPermutations(i+1)`, and then pop the last character from `temp`.
    # 3. Start the recursion with `binaryPermutations(0)`.
    # 4. Return `ans` containing all the generated binary string permutations.

def binaryStrings(string):    
    ans, temp = [], []
    def binaryPermutations(i):
        if i == len(string):
            ans.append("".join(temp))
            return

        if string[i] == "?":
            temp.append('0')
            binaryPermutations(i + 1)
            temp.pop()
            temp.append('1')
            binaryPermutations(i + 1)
            temp.pop()
        else:
            temp.append(string[i])
            binaryPermutations(i + 1)
            temp.pop()

    binaryPermutations(0)
    return ans
