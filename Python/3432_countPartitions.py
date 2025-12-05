class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        rightTotal = sum(nums)
        partitions = 0
        for i in range(len(nums)-1):
            rightTotal -= (nums[i]*2)
            if rightTotal % 2 == 0:
                partitions+=1
        return partitions
