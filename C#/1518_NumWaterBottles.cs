public class Solution {
    public int NumWaterBottles(int numBottles, int numExchange) {
        int drankTotal = numBottles;
        int numEmpty = numBottles;
        while(numEmpty >= numExchange){
            drankTotal += numEmpty / numExchange;
            numEmpty = (numEmpty % numExchange) + (numEmpty / numExchange);
        }
            
        return drankTotal;
    }
}
