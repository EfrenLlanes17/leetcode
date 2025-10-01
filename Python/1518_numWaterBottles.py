class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drankTotal = numBottles
        numEmpty = numBottles
        while numEmpty >= numExchange:
            drankTotal += numEmpty // numExchange
            numEmpty = (numEmpty % numExchange) + (numEmpty // numExchange)
            
        return drankTotal
