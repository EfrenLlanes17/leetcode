class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        prevWord = ""
        result = []
        for i in range(len(words)):
           sortedWord = sorted(words[i])
           if prevWord != sortedWord:
             result.append(words[i])
           prevWord = sortedWord
        return result
