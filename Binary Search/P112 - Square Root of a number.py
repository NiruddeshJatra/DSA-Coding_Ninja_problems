def floorSqrt(n):
   l, r = 1, n
   while l <=r:
      mid = (l+r)//2
      if mid*mid > n:
         r = mid - 1
      else:
         l = mid + 1

   return l-1
