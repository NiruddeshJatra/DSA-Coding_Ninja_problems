def bored_chef(n: int, k: int, s: str) -> int:
    freq = Counter(s)
    if max(freq.values()) >= k:
        return 1
    return 0
