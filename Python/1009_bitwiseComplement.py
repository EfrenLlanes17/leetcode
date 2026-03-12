class Solution(object):
    def bitwiseComplement(self, n):
        num = 1
        while n >= num*2:
            num*=2
        count = 0
        while num != 0:
            if num - n > 0:
                count+=num
            else:
                n -= num
            num/=2
        return count

        
        
