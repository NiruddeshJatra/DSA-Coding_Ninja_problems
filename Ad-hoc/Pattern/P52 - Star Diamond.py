def nStarDiamond(n: int) -> None:
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,2*i):
            print("*", end="")
        print("\n")
        
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range(2*(n-i)-1):
            print("*", end="")
        print(" \n")
    
