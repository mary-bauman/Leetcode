class Solution:
    def punishmentNumber(self, n: int) -> int:
        def all_partitions(s):
            for cutpoints in range(1 << (len(s)-1)):
                result = []
                lastcut = 0
                for i in range(len(s)-1):
                    if (1<<i) & cutpoints != 0:
                        result.append(int(s[lastcut:(i+1)]))
                        lastcut = i+1
                result.append(int(s[lastcut:]))
                yield sum(result)

        punish = 0
        for i in range(1,n+1):
            if i in all_partitions(str(i*i)): punish += (i*i)  
        return punish
