class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        #trim the beginning
        while s1 and s2 and s1[0]==s2[0]:
            s1, s2 = s1[1:], s2[1:]

        #trim the end
        while s1 and s2 and s1[-1]==s2[-1]:
            s1, s2 = s1[:-1], s2[:-1]

        return not (s1 and s2)
        

        
