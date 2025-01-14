import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for (int a = 0; a < n-1; a++){
            for (int b = a+1; b < n; b++){
                if ((nums[a]+nums[b]==target)){
                    return new int[]{a, b};
                }
            }
        }
        return new int[]{0,0};
    }
}
