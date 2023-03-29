import java.util.ArrayList;
import java.util.List;
import java.util.Stack;;


class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    
    public List<List<Integer>> permute(int[] nums) {
        Stack<Integer> track = new Stack<Integer>();
        dfs(nums, track);
        return res;

    }

    private void dfs(int[] nums, Stack<Integer> track) {
        if (nums.length == track.size()) {
            res.add(new ArrayList<>(track));
            return;
        }

        for (int num : nums) {
            if (!track.contains(num)) {
                track.add(num);
                dfs(nums, track);
                track.pop();
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<List<Integer>> result = solution.permute(new int[] {1,2,3,});
        System.out.println(result);
    }

}