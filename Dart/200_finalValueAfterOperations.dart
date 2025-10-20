class Solution {
  int finalValueAfterOperations(List<String> operations) {
     int x = 0;
        for(String s in operations){
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
