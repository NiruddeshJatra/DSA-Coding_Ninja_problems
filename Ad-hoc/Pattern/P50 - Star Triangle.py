def nStarTriangle(n: int) -> None:
    for i in range(1,1+n):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,2*i):
            print("*", end="")
        print(" \n")
