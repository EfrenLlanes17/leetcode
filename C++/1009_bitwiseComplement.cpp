class Solution {
public:
    int bitwiseComplement(int n) {
        int num = 1;
        while(n >= num*2)
            num*=2;
        int count = 0;
        while(num != 0){
            if(num - n > 0)
                count+=num;
            else
                n -= num;
            num/=2;
        }
        return count;
    }
};
