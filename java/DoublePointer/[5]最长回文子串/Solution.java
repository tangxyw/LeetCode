class Solution {
    public String longestPalindrome(String s) {
        int max_length = 0, max_start = 0;
        int n = s.length();
        for (int i = 0; i < n; i++) {
            int left = i - 1, right = i + 1;
            int length = 1;

            while (left >= 0 && s.charAt(left) == s.charAt(i)) {
                left--;
                length++;
            }

            while (right < n && s.charAt(right) == s.charAt(i)) {
                right++;
                length++;
            }

            while (left >= 0 && right < n && s.charAt(left) == s.charAt(right)) {
                left--;
                right++;
                length = length + 2;
            }

            if (length > max_length) {
                max_length = length;
                max_start = left + 1;
            }

        }
        return s.substring(max_start, max_start+max_length);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String result = solution.longestPalindrome("babad");
        System.out.println(result); 
    }
}