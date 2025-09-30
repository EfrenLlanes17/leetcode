class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(None)
        def helper(i,j):
            if i+2 > j: 
                return 0
            if i+2 == j:
                return values[i] * values[i+1] * values[j]

            return min(
                ((values[i]*values[k] * values[j]) + helper(i,k) + helper(k,j))
                for k in range(i+1,j)
            )
        return helper(0, len(values)-1)

            
            
