class Solution:
    def trap(self, height: List[int]) -> int:
        sm = 0
        n = len(height)
        pre = [0] * n
        suf = [0] * n

        pre[0] = height[0]

        for i in range(1, n):
            pre[i] = max(pre[i - 1], height[i])

        suf[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i + 1], height[i])

        for i in range(n):
            sm += min(suf[i], pre[i]) - height[i]

        return sm
