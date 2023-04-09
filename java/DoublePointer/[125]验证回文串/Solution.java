class Solution {
    public boolean isPalindrome(String s) {
        StringBuffer sgood = new StringBuffer();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isLetterOrDigit(c)) sgood.append(Character.toLowerCase(c));
        }

        int left = 0, right = sgood.length() - 1;

        while (left < right) {
            if (sgood.charAt(left) != sgood.charAt(right)) return false;
            left++;
            right--;
        }

        return true;
    }
}