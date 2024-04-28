class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #three liner
        cur = [[1]]
        for i in range(rowIndex): cur.append([1] + [cur[-1][i] + cur[-1][i+1] for i in range(len(cur[-1])-1)] + [1])
        return cur[-1]

        #actual solution
        cur = [[1]]
        for i in range(rowIndex):
            c = cur[-1]
            row = [1] + [c[i] + c[i+1] for i in range(len(c)-1)] + [1]
            cur.append(row)
        return cur[-1]
