class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans, prev = [words[0]], groups[0]
        for i in range(1,len(words)):
            if groups[i] != prev:
                ans.append(words[i])
                prev = not(prev)
            

        return ans
        
