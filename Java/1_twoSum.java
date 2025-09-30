class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        for(int x = 0; x < nums.length;x++){
           for(int a = 1; a+x <nums.length;a++){
              if( nums[x] + nums[x+a] == target){
                  result[0] = x;
                  result[1] = a+x;

              }
            
           }

        }
        return result;
    }
}
