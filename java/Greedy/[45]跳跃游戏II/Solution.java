class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int right = 0;
        int max_far = 0;
        int step = 0;

        for (int i = 0; i < n - 1; i++) {
            max_far = Math.max(max_far, nums[i] + i);
            if (i == right) {
                right = max_far;
                step++;
                if (right >= n - 1) break;
            }
        }

        return step;
    }
}