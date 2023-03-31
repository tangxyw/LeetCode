import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<String> res = new ArrayList<String>();

    public List<String> generateParenthesis(int n) {        
        dfs(0, 0, n, "");
        return res;
    }

    private void dfs(int left, int right, int n, String track) {
        if (left == n && right == n) {
            res.add(track);
            return;
        }

        if (left < right || left > n ) return;

        dfs(left+1, right, n, track+"(");
        dfs(left, right+1, n, track+")");
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<String> res = solution.generateParenthesis(3);
        System.out.println(res);
    }
}