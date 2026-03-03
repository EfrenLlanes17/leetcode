class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        countList = []
        for row in grid:
            count = 0
            for i in range(n - 1, -1, -1):
                if row[i] == 0:
                    count += 1
                else:
                    break
            countList.append(count)

        swapCount = 0

        for i in range(n):
            required = n - 1 - i
            j = i
            while j < n and countList[j] < required:
                j += 1

            if j == n:
                return -1

            while j > i:
                countList[j], countList[j - 1] = countList[j - 1], countList[j]
                swapCount += 1
                j -= 1

        return swapCount
