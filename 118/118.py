class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        #three liner
        cur = [[1]]
        for i in range(1,numRows): cur.append([1] + [cur[-1][i] + cur[-1][i+1] for i in range(len(cur[-1])-1)] + [1])
        return cur

        #actual solution
        cur = [[1]]
        for i in range(1,numRows):
            c = cur[-1]
            row = [1] + [c[i] + c[i+1] for i in range(len(c)-1)] + [1]
            cur.append(row)
        return cur
