class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<char> longest;
        vector<char> curr;
        for(char c : s){
            if(find(curr.begin(), curr.end(), c) == curr.end()){
                curr.insert(curr.end(), c);
                if(longest.size() < curr.size()){
                    longest = curr;
                }
            }
            else{
                for(int i = 0; i < curr.size(); ++i){
                    if(curr[i] == c){
                        curr.erase(curr.begin(), curr.begin() + i + 1);
                        curr.insert(curr.end(), c);
                        goto end;
                    }
                }
                curr.clear();
                curr.insert(curr.end(), c);
                end:
            }
        }
        return longest.size();
    }
};
