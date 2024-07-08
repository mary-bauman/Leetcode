class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empty = numBottles
        while empty >= numExchange:
            filled = empty // numExchange
            empty = (empty % numExchange) + filled
            drank += filled
        return drank
