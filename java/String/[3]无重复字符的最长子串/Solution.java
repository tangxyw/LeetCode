import java.util.HashMap;
import java.util.Map;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), res = 0;
        Map<Character, Integer> hashtable = new HashMap<Character, Integer>();
        int left = 0, right = 0;

        while (right < n) {
            char c = s.charAt(right);
            right++;
            hashtable.put(c, hashtable.getOrDefault(c, 0)+1);

            while (hashtable.getOrDefault(c, 0) > 1) {
                char d = s.charAt(left);
                hashtable.put(d, hashtable.get(d) - 1);
                left++;
            }   
            res = Math.max(res, right - left);
        }
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.lengthOfLongestSubstring("abcbcabb"); 
        System.out.println(result);
    }
}