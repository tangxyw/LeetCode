import java.util.Arrays;

class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        int squares_count = (int) Math.sqrt(n+1);
        int[] squares = new int[squares_count];
        for (int i = 0; i < squares_count; i++) {
            squares[i] = (i+1)*(i+1);
        }

        for (int j = 1; j < n+1; j++) {
            for (int x : squares) {
                if (j >= x) {
                    dp[j] = Math.min(dp[j], dp[j-x] + 1);
                }
            }
        }

        return dp[n];
    }
}