class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastOneIndex = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if lastOneIndex != -1 and i - lastOneIndex -1 < k:
                    return False
                lastOneIndex = i

        return True
