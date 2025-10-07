class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = []
        numSet = set(nums)
        for i in range(1,len(nums)+1):
            if i not in numSet:
                output.append(i)
        return output
