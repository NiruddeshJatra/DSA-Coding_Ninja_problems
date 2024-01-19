# time_complexity: O(1)
# space_complexity: O(1)


#Process

# 1. Find a = the cubic root of n

# 2. If a is an integer, there will be only one way: 0^3+(cubic root of n)^3

# 3. Else we can take the integer value of a, cube it and subtract it from n. Then find b = the cubic root of the subtracted number. If b is an integer, then int(a)^3 + b^3 = n. If a=b, there will one possible way, otherwise there will be two distict pair (a,b),(b,a), meaning two possibilities.

# 4. Else there will be no possibility.

def countCubeSumPairs(n):
    a = n**(1/3)
    b = (n-(int(a)**3))**(1/3)
    
    if a.is_integer():
        return 1
     
    elif b.is_integer():
        if int(a)!=int(b):
            return 2
          
        else:
            return 1
           
    else:
        return 0
                 
                    
t = int(input())
for _ in range(t):
    n = int(input())
    print(countCubeSumPairs(n))
    




    

