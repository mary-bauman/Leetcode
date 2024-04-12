class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        s1 = deque()
        lowestHeight = inf
        for i, h in enumerate(height):
            if s1 and h > lowestHeight:
                while s1 and s1[-1][0] < h:
                    lowestHeight = min(s1[-1][0], lowestHeight)
                    if s1[-1][0] > lowestHeight:
                        ans += (min(h, s1[-1][0])-lowestHeight) * (i-s1[-1][1]-1)
                        lowestHeight = min(h,s1[-1][0])
                    s1.pop()
                if s1:
                    ans += (min(h, s1[-1][0])-lowestHeight) * (i-s1[-1][1]-1)
                    lowestHeight = min(h,s1[-1][0])
            s1.append((h,i))
            lowestHeight = min(h, lowestHeight)
        return ans
