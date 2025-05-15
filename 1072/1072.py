class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patternFreq = defaultdict(int)

        for curRow in matrix:
            # Convert row to pattern using list comprehension and join
            # 'T' if element matches first element, 'F' otherwise
            row_pattern = "".join(
                "T" if num == curRow[0] else "F" for num in curRow
            )
            patternFreq[row_pattern] += 1

        return max(patternFreq.values(), default=0)
