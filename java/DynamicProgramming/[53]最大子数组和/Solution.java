class Solution {
    public int maxSubArray(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        int res = nums[0];
        dp[0] = nums[0];

        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(dp[i-1] + nums[i], nums[i]);
            res = Math.max(res, dp[i]);
        }

        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.maxSubArray(new int[] {-2,1,-3,4,-1,2,1,-5,4});
        System.out.print(result);
    }
}