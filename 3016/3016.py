class Solution:
    def minimumPushes(self, word: str) -> int:
        total = 0
        increment = 1
        incNum = 0
        c = Counter(word).most_common()
        for char, count in c:
            total+=count*increment
            incNum+=1
            if incNum==8:
                increment += 1
                incNum = 0
        return total
        
