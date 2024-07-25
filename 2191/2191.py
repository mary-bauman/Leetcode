class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        both = []
        for num in nums:
            mapped = int(''.join(str(mapping[int(digit)]) for digit in str(num)))
            y = int(''.join(map(str, [int(n) for n in str(num)])))
            both.append([mapped, y])
        both.sort(key=lambda x: x[0])        
        return [b for [a,b] in both]
