class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        vector<int> answer;
        for(int i = nums.size()-1; i >= 0; --i){
            while(nums[i] != 0){
                answer.push_back(nums[i]%10);
                nums[i]/=10;
            }
        }
        reverse(answer.begin(), answer.end());
        return answer;
    }
};
