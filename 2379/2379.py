class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        #looking for the blackest block of size k
        #then return amount of whites
        curBlacks = (blocks[:k]).count("B")
        biggestBlacks = curBlacks
        prev = blocks[k-1]
        for i in range(k,n):
            cur = blocks[i]
            prev = blocks[i-k]

            if prev=="B":
                if cur =="W": curBlacks-=1
            else:
                if cur =="B": curBlacks+=1

            biggestBlacks = max(biggestBlacks, curBlacks)

        return k-biggestBlacks
        
