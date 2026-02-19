class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        previous = 0
        current = 1
        total = 0
        for i in range(len(s)-1):
            if(s[i] == s[i+1]):
                current+= 1
            else:
                total += min(current,previous)
                previous = current
                current = 1
        return total + min(current,previous)
