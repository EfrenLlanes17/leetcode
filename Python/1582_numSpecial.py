class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        mOnes = [0] * len(mat)
        nOnes = [0] * len(mat[0])

        for i in range(len(mat)):  
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    mOnes[i] += 1
                    nOnes[j] +=1

        count = 0
        for i in range(len(mat)):  
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and mOnes[i] == 1 and nOnes[j] == 1:
                    count+=1
        return count
