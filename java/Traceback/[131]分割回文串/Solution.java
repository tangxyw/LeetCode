import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    private List<List<String>> res = new ArrayList<>();
    private int n;

    public List<List<String>> partition(String s) {
        this.n = s.length();
        Stack<String> track = new Stack<String>();

        traceback(s, 0, track);

        return res;
    }

    private void traceback(String s, int index, Stack<String> track) {
        if (index == n) {
            res.add(new ArrayList<>(track));
            return;
        }

        for (int i = index; i < n; i++) {
            if (isSymmetry(s, index, i) == true) {
                track.add(s.substring(index, i+1));
                traceback(s, i+1, track);
                track.pop();
            }
        }
    }

    private boolean isSymmetry(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) return false;
            left++;
            right--; 
        }
        return true;
    }
}