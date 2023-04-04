class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        s = " " + s;
        char[] cs = s.toCharArray();
        int[] dp = new int[n+1];
        dp[0] = 1;

        for (int i = 1; i < n+1; i++) {
            int a = cs[i] - '0';
            int b = (cs[i-1] - '0') * 10 + a;
            if (a >= 1 && a <= 9) dp[i] += dp[i-1];
            if (b >= 10 && b <= 26) dp[i] += dp[i-2];
        }
        return dp[n];
    }
}