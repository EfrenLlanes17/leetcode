class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        dayPay = 1
        for i in range(1,n+1):
            total += dayPay
            if(i%7 == 0):
                dayPay = (i//7)
            dayPay+=1
        return total
