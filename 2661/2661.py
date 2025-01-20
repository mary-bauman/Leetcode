class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        cols = defaultdict(int)
        rows = defaultdict(int)

        locations = {col: (r, c) for r, row in enumerate(mat) for c, col in enumerate(row)}

        for i in range(len(arr)):
            a = arr[i]
            r,c = locations[a]
            rows[r] += 1
            if rows[r] == n: return i
            cols[c] += 1
            if cols[c] == m: return i            
