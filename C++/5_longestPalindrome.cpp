class Solution {
public:
    string longestPalindrome(string s) {
        int start = 0;
        int len = 0;
        for(int i = 0; i < s.size(); ++i){
            for(int j = 0; i+j < s.size() && i-j >= 0 && s[i-j] == s[i+j];++j){
                if(len < j+1+j){
                    start = i-j;
                    len = j+1+j;
                }
            }
            for(int j = 0; i+j+1 < s.size() && i-j >= 0 && s[i-j] == s[i+j+1];++j){
                if(len < j+2+j){
                    start = i-j;
                    len = j+2+j;
                }
            }
        }

        return s.substr(start, len);
    }
};
