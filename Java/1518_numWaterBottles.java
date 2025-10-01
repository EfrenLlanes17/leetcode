class Solution {
    public int numWaterBottles(int numBottles, int numExchange) {
        int drankTotal = numBottles;
        int numEmpty = numBottles;
        while(numEmpty >= numExchange){
            drankTotal += numEmpty / numExchange;
            numEmpty = (numEmpty % numExchange) + (numEmpty / numExchange);
        }
            
        return drankTotal;
    }
}
