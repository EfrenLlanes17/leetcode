class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        char lastOneIndex = -1;
        for(char i = 0; i < nums.size(); i++){
            if(nums[i] == 1){
                if(lastOneIndex != -1 && i - lastOneIndex -1 < k){
                    return false;
                }
                lastOneIndex = i;
            }
        }
        return true;
    }
};
