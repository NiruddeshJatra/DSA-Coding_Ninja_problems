def checkPalindrome(N)->bool:
    binaryOfN = bin(N)[2:]
    if binaryOfN == binaryOfN[::-1]:
        return True
    return False
