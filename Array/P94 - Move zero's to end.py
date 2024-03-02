def moveZeros(n: int,  a: [int]) -> [int]:
    nums = []
    for i in a:
        if i != 0:
            nums.append(i)
    
    for i in range(len(a)-len(nums)):
        nums.append(0)

    return nums
