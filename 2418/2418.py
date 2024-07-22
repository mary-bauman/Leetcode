class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for (num,name) in sorted(zip(heights,names), reverse=True)]
        
