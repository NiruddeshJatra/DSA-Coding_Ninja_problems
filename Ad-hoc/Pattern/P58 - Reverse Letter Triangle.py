def nLetterTriangle(n: int):
    for i in range(n):
        for j in range(n-i):
            print(chr(ord('A')+j),end=" ")
        print(" \n")
