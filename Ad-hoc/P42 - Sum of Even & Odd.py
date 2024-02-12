num = input()
oddSum, evenSum = 0,0
for i in num:
    if int(i)%2 == 0:
        evenSum += int(i)
    else:
        oddSum += int(i)
print(evenSum,oddSum)
