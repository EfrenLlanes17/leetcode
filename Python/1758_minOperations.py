class Solution:
    def minOperations(self, s: str) -> int:
        startZ = 0
        for i in range(len(s)):
            if s[i] == "01"[i%2]:
                startZ+=1
        return min(len(s) -startZ ,startZ)
