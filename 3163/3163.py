class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 1
        char = word[0]
        for w in word[1:]:
            if char==w and count<9: count+=1
            else:
                comp += str(count) + char
                count = 1
                char = w
        return comp + str(count) + char
