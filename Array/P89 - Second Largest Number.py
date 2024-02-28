def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    a = list(set(a))
    a.remove(max(a))
    a.remove(min(a))
    return [max(a),min(a)]
