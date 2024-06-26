class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #algo from https://leetcode.com/u/bhanu_bhakta/
        # s = "aab|"
        # a, ab -> No
        # a, b, c -> Yes
        # aa, b -> Yes
        # aab -> No
        # [[a, b, c], [aa, b]] -> Output
        # SOLUTION
        # TC: 2^N
        # SC: 2^N

        result = []
        n = len(s)

        def explore(index, curr):
            if index >= n:
                result.append(curr.copy())

            for i in range(index, n):
                subStr = s[index:i + 1]
                if subStr == subStr[::-1]:
                    curr.append(subStr)
                    explore(i + 1, curr)
                    curr.pop()

        explore(0, [])
        return result
