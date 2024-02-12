def numberCrown(n: int) -> None:
    for i in range(1,1+n):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(2*(n-i)):
            print(" ",end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        print("\n")
