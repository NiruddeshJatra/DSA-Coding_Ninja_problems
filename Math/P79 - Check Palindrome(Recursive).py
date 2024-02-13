def isPalindrome(string: str) -> bool:
    if string == string[::-1]:
        return True
    return False
