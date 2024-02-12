def nStarTriangle(n: int) -> None:
    for i in range(1,n+1):
        for j in range(i):
            print("*",end="")
        print("\n")
    for i in range(n-1):
        for j in range(n-1-i,0,-1):
            print("*",end="")
        print("\n")
        
