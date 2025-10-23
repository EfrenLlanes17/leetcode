class Solution {
public:
    bool hasSameDigits(string s) {       
        do{
            string x;
            for(int i = 0; i < s.length()-1; i++){
                x+= (s[i] + s[i+1] -96) % 10;
            }
            s= x;
        }while(s.length() != 2);

        if(s[0] == s[1]){
            return true;
        }
        return false;
    }
};
