class Solution {
public:
    int totalMoney(int n) {
        int total = 0;
        int dayPay = 1;
        for(int i = 1; i <= n; i++){
            total += dayPay;
            if(i%7 == 0)
                dayPay = (i/7);
            dayPay+=1;
        }
        return total;
        
    }
};
