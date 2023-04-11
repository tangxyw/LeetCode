class Solution {
    public int maxProduct(int[] nums) {
        int n = nums.length;
        int[][] dp = new int[2][n];

        dp[0][0] = nums[0];
        dp[1][0] = nums[0];

        int res = dp[1][0];

        for (int i = 1; i < n; i++) {
            if (nums[i] > 0) {
                dp[0][i] = Math.min(dp[0][i-1] * nums[i], nums[i]);
                dp[1][i] = Math.max(dp[1][i-1] * nums[i], nums[i]); 
            } else {
                dp[0][i] = Math.min(dp[1][i-1] * nums[i], nums[i]);
                dp[1][i] = Math.max(dp[0][i-1] * nums[i], nums[i]); 
            }
            res = Math.max(res, dp[1][i]);            
        }

        return res;
    }
}