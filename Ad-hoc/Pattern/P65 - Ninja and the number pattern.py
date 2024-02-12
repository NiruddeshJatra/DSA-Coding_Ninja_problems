def getNumberPattern(n: int) -> None:
    for i in range(2*n-1):
        for j in range(2*n-1):
            up = i
            down = 2*(n-1)-i
            left = j
            right = 2*(n-1)-j
            print(n-min(up,down,left,right),end="")
        print("\n")
