class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxNum = 0
        while left != right:
            maxNum = max(maxNum,(min(height[left],height[right])*(right-left)))
            if min(height[left],height[right]) == height[right]:
                right -=1
            else:
                left +=1


        return maxNum
