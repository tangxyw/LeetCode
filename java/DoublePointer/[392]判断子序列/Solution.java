class Solution {
    public boolean isSubsequence(String s, String t) {
        int m = s.length(), n = t.length();

        int p = 0, q = 0;

        while (p < m && q < n) {
            if (s.charAt(p) == t.charAt(q)) {
                p++;
            }
            q++;
        }

        return p == m;  
    }
}