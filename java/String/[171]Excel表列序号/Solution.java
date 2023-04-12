class Solution {
    public int titleToNumber(String columnTitle) {
        int n = columnTitle.length();
        int multipler = 1;
        int sum = 0;

        for (int i = 1; i <= n; i++) {
            sum += (columnTitle.charAt(n-i) - 'A' + 1) * multipler;
            multipler *= 26;
        }

        return sum;
    }
}