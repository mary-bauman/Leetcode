class Solution(object):
    def findComplement(self, num):
        mask = (1 << num.bit_length()) - 1
        return num ^ mask
        
