class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& boxGrid) {
        vector<vector<char>> result(boxGrid[0].size(), vector<char>(boxGrid.size()));
        for(int row = 0; row < boxGrid.size(); ++row){
            char prev = '*';
            int gapCount = 0;
            for(int col = boxGrid[row].size()-1; col >= 0 ; --col){
                char curr = boxGrid[row][col];
                if(prev == '.' ){
                    if(curr == '#'){  
                        result[col+1 + gapCount][boxGrid.size()-row-1] = '#';
                        curr = '.';
                    }
                    else if(curr == '.'){
                        gapCount++;
                    }
                    else{
                        gapCount = 0;
                    }
                }
                result[col][boxGrid.size()- row-1] = curr;
                prev = curr;
            }
        }

        return result;
    }
};
