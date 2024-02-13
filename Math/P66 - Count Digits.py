def countDigits(n: int) -> int:
    count = 0
    num = list(str(n))
    for i in num:
        if int(i) and n%int(i)==0:
            count+=1
    return count
