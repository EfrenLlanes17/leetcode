class Solution {
public:
    int maxNumberOfBalloons(string text) {
        int bNum = 0, aNum = 0, lNum = 0, oNum = 0, nNum = 0;

        for(char c : text){
            switch(c){
                case 'b':
                    bNum+=1;
                    break;
                case 'a':
                    aNum+=1;
                    break;
                case 'l':
                    lNum+=1;
                    break;
                case 'o':
                    oNum+=1;
                    break;
                case 'n':
                    nNum+=1;
                    break;
                default:
                    break;
            }
        }
        return std::min({bNum, aNum, lNum/2, oNum/2, nNum});
    }
};
