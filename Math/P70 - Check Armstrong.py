num = input()
total = 0
length = len(num)
for i in num:
    total += int(i)**length

if int(num)==total:
    print("true")
else:
    print("false")
