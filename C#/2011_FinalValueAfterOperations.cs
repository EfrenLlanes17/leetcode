public class Solution {
    public int FinalValueAfterOperations(string[] operations) {
        int x = 0;
        foreach(string s in operations){
            if(s[1] == '-'){
                x--;
            }
            else{
                x++;
            }
        }
        return x;
    }
}
