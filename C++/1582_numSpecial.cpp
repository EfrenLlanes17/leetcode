class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        vector<int> mOnes(mat.size(), 0);
        vector<int> nOnes(mat[0].size(), 0);

        for(int i = 0; i < mat.size(); i++){  
            for(int j = 0; j < mat[0].size(); j++){
                if(mat[i][j] == 1){
                    mOnes[i] += 1;
                    nOnes[j] +=1;
                }
            }
        }
        int count = 0;
        for(int i = 0; i < mat.size(); i++){  
            for(int j = 0; j < mat[0].size(); j++){
                if(mat[i][j] == 1 && mOnes[i] == 1 && nOnes[j] == 1){
                    count++;
                }
            }
        }
        return count;
    }
};
