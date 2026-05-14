class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if i+1 != nums[i]:
                return False

        return len(nums)-1 == nums[-1]
