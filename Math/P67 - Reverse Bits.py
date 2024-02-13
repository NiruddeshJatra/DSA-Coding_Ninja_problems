def reverseBits(n):
    binary = (bin(n)[2:]).zfill(32)
    reversedBin = binary[::-1]
    return int(reversedBin,2)

