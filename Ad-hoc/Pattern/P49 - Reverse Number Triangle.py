def nNumberTriangle(n: int) -> None:
    for i in range(n):
        x = 1
        for j in range(n-i,0,-1):
            print(x,end=" ")
            x += 1
        print("\n")
