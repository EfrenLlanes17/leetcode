class Solution {
public:
    int minOperations(string s) {
        int startZ = 0;
        for(int i = 0; i < s.size(); i++)
            if (s[i] == "01"[i%2]) 
                startZ++;
        return min((int)s.size() -startZ ,startZ);
    }
};
