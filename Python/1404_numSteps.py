class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        s = list(s)
        while len(s) != 1:
            if s[len(s) -1] == "1":
                index = len(s) -1
                found = False
                while index >= 0:
                    if s[index] == "0":
                        s[index] = "1"
                        found = True
                        break
                    else:
                        s[index] = "0"
                    index-=1
                if not found:
                    s.insert(0, "1")
                
            else:
                s.pop()
            count+=1
        return count

