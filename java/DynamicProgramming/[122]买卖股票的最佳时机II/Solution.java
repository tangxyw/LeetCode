class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[2][n];

        dp[0][0] = 0;
        dp[1][0] = -prices[0];

        for (int i = 1; i < n; i++) {
            dp[0][i] = Math.max(dp[0][i-1], dp[1][i-1] + prices[i]);
            dp[1][i] = Math.max(dp[1][i-1], dp[0][i-1] - prices[i]);
        }
        return dp[0][n-1];
    }
}