import java.util.HashSet;
import java.util.List;
import java.util.Set;


class Solution {
    private boolean global_res = false;
    private Set<Integer> memo = new HashSet<Integer>();
    private int n;
    private List<String> wordDict;

    public boolean wordBreak(String s, List<String> wordDict) {
        this.n = s.length();
        this.wordDict = wordDict;

        dfs(s, 0);

        return global_res;
    }

    private boolean dfs(String s, int start) {
        if (global_res == true) return true;

        if (start == n) {
            global_res = true;
            return true;
        }

        if (memo.contains(start)) return false;

        boolean dfs_res = false;
        for (int i = start; i <= n; i++) {
            if (wordDict.contains(s.substring(start, i))) {
                dfs_res = dfs(s, i) || dfs_res;
            }
        }
        if (dfs_res == false) memo.add(start);

        return dfs_res;
    }
}