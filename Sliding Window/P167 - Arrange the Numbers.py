def maximumSubarraySum(n: int, v: list[int]) -> int:
   total = 0
   for num in v:
      if num > 0:
         total += num

   return total
