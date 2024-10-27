# This is a genius problem. To solve it, you need to think out of the box. 
# Here, the numbers in each cell represent the minimum distance from each border to that cell. 
# Once you understand this, the job is done.

def getNumberPattern(n: int) -> None:
    for i in range(2*n-1):
        for j in range(2*n-1):
            up = i
            down = 2*(n-1)-i
            left = j
            right = 2*(n-1)-j
            print(n-min(up,down,left,right),end="")
        print("\n")
