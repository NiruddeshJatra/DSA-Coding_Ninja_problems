# Time Complexity: O(nlogn)
# Space Complexity: O(1)


def minProduct(arr: list, n: int, k: int) -> int:
	arr.sort()
	ans = 1
	for i in range(k):
		ans *= arr[i]

	return ans%(10**9+7)
