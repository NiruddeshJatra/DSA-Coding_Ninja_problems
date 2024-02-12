def alphaHill(n: int):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(i+1):
            print(chr(ord('A')+j),end=" ")
        for j in range(i-1,-1,-1):
            print(chr(ord('A')+j),end=" ")
        print(" \n")
            
            
            
            
            
            
            
