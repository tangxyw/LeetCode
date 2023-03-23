class Solution {
    public String longestCommonPrefix(String[] strs) {
        String res = strs[0];
        
        for (int i = 1; i < strs.length; i++) {
            int j = 0;
            while (j < Math.min(res.length(), strs[i].length())) {
                if (res.charAt(j) != strs[i].charAt(j)) {
                    break;
                }
                j++;
            }
            res = res.substring(0, j);
        }
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String result = solution.longestCommonPrefix(new String[] {"flower","flow","flight"});
        System.out.println(result);
    }
}