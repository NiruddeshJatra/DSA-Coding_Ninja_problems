def nNumberTriangle(n: int) -> None:
    x = 1
    for i in range(1,1+n):
        for j in range(i):
            print(x,end=" ")
            x+=1
        print("\n")
