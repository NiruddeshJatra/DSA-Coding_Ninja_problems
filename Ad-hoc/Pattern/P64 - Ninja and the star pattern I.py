def getStarPattern(n: int) -> None:
    s = '*'*n
    print(s)
    for i in range(n-2):
        print("*",end="")
        for j in range(n-2):
            print(" ",end="")
        print("*")
    if n>1:
    	print(s)
              
