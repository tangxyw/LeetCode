import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;

class Solution {
    List<List<Integer>> res = new ArrayList<>();
    Stack<Integer> track = new Stack<Integer>();
    boolean[] visited;
    int n;
    int[] nums;

    public List<List<Integer>> permuteUnique(int[] nums) {
        this.nums = nums;
        this.n = nums.length;
        this.visited = new boolean[n];
        Arrays.sort(nums);

        traceback(0, track);

        return res;

    }

    private void traceback(int depth, Stack<Integer> track) {
        if (depth == n) {
            res.add(new ArrayList<>(track));
            return;
        }
            
        for (int i = 0; i < n; i++) {
            if (visited[i] || (i > 0 && nums[i-1] == nums[i] && !visited[i-1])) continue;
            visited[i] = true;
            track.add(nums[i]);
            traceback(depth+1, track);
            track.pop();
            visited[i] = false;
        }
    }
}