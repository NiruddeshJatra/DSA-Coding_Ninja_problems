def nBinaryTriangle(n: int) -> None:
    for i in range(1,1+n):
        x = 0 if i%2==0 else 1
        for j in range(i):
            print(x,end=" ")
            x = 0 if x else 1
        print("\n")
        
