class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [x for x in range(1, n + 1)]
        curIndex = k - 1
        for i in range(n - 1):
            arr.pop(curIndex)
            curIndex = (curIndex + k - 1) % len(arr)
        return arr[0]

