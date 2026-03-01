class Solution {
public:
    int minPartitions(string n) {
        char max ='1';
        for(char c : n){
            if(c > max){
                max = c;
            }
        }
        return max - '0';
    }
};
