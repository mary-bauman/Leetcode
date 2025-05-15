class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if five<0 or ten<0: return False
            if bill==5: five+=1
            elif bill==10: 
                five-=1
                ten+=1
            else:
                if ten==0: five-=3
                else:
                    five-=1
                    ten-=1        
        return (five>=0 and ten>=0)


        
