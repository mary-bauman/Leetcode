class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        candidates.sort()
        count = Counter(candidates)

        for c in candidates:
            for i in range(c, target+1):
                if not dp[i-c]: continue

                for x in dp[i-c]:
                    if Counter(x)[c] >= count[c]: continue
                    if x+[c] in dp[i]:
                        dp[i].append(x+[c])

            if c <= target:
                dp[c].append([c])

        for i,d in enumerate(dp):
            print(i, d)            
        
        return dp[target]
