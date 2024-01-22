# Time Complexity: O(n)
# Space Complexity: O(1)

def divideByFour(arr):
    for i in range(len(arr)):
        arr[i]//=4
        if arr[i]==0:
            arr[i]=-1
