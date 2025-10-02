class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numEmpty = numBottles
        while(numEmpty >= numExchange):
                numBottles+=1
                numEmpty = (numEmpty - numExchange) +1
                numExchange+=1
            
        return numBottles
