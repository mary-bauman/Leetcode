class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        #land first
        #get earliest land end time
        earliestLandEnd = inf
        for i in range(len(landStartTime)):
            earliestLandEnd = min(earliestLandEnd, landStartTime[i]+landDuration[i])
        #now earliest water that starts after earliestLandEnd
        option1 = inf
        for i in range(len(waterStartTime)):
            if waterStartTime[i]>=earliestLandEnd:
                option1 = min(option1, waterStartTime[i]+waterDuration[i])
            else:
                option1 = min(option1, waterDuration[i]+earliestLandEnd)

        #water first
        earliestWaterEnd = inf
        for i in range(len(waterStartTime)):
            earliestWaterEnd = min(earliestWaterEnd, waterStartTime[i]+waterDuration[i])
        option2 = inf
        for i in range(len(landStartTime)):
            if landStartTime[i]>=earliestWaterEnd:
                option2 = min(option2, landStartTime[i]+landDuration[i])
            else:
                option2 = min(option2, landDuration[i]+earliestWaterEnd)

        return min(option1, option2)
        
