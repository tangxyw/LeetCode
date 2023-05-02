import java.util.*;

class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private int[] nums;
    private int n;

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        this.nums = nums;
        this.n = nums.length;
        
        Stack<Integer> track = new Stack<Integer>();

        tracback(0, track);

        return res;
    }

    private void tracback(int index, Stack<Integer> track) {        
        
        res.add(new ArrayList<>(track));
        
        if (index == n) return;

        for (int i = index; i < n; i++) {
            if (i > index && nums[i-1] == nums[i]) continue;
            track.add(nums[i]);
            tracback(i+1, track);
            track.pop();
        }
    }
}