class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: return [0 for _ in range(len(code))]
        if k < 0:
            code2 = []
            total = sum(code[len(code)+k:])
            for i in range(len(code)):
                code2.append(total)
                total += code[i] - code[i+k]
            return code2
        #k>0
        code2 = []
        total = sum(code[1:1+k])
        for i in range(-len(code), 0):
            code2.append(total)
            total += code[i+1+k]-code[i+1]
        return code2
        
