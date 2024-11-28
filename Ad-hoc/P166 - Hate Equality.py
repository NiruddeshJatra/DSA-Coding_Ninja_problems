def canYouMakeDifference(n: int, s: str) -> int:
    if len(set(s)) == 1:
        return 0
    return 1
