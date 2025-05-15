class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
      #please note this is stupid bad code for the sake of making it successful in one line
        return [b for a, b in sorted([[int(''.join(str(mapping[int(digit)]) for digit in str(num))), int(''.join(map(str, [int(n) for n in str(num)])))] for num in nums], key=lambda x: x[0])]
