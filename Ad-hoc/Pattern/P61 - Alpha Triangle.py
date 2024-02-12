def alphaTriangle(n: int):
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('A')+n-j-1),end=" ")
        print(" \n")
    
