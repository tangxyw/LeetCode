import java.util.*;

class Solution {
    private List<List<Integer>> res = new ArrayList<>();
    private int[] candidates;
    private int n;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        this.candidates = candidates;
        this.n = candidates.length;

        Stack<Integer> track = new Stack<Integer>();

        traceback(0, track, target);

        return res;

    }

    private void traceback(int index, Stack<Integer> track, int target) {
        if (target == 0) {
            res.add(new ArrayList<>(track));
            return;
        }

        for (int i = index; i < n; i++) {
            if (candidates[i] <= target) {
                track.add(candidates[i]);
                traceback(i, track, target - candidates[i]);
                track.pop();
            } else break;
        }

    }
}