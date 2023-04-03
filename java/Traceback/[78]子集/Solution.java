import java.util.ArrayList;
import java.util.Stack;
import java.util.List;


class Solution {
    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        Stack<Integer> track = new Stack<Integer>();
        traceback(nums, 0, track);
        return res;
    }

    private void traceback(int[] nums, int index, Stack<Integer> track) {
        res.add(new ArrayList<>(track));

        if (index == nums.length) return;

        for (int i = index; i < nums.length; i++) {
            track.add(nums[i]);
            traceback(nums, i+1, track);
            track.pop();
        }
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<List<Integer>> res = solution.subsets(new int[] {1,2,3});
        System.out.println(res);
    }
}