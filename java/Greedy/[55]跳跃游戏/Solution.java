class Solution {
    public boolean canJump(int[] nums) {
        int max_distance = 0;

        for (int i = 0; i < nums.length; i++) {
            if (i > max_distance) return false;
            max_distance = Math.max(max_distance, nums[i]+i);
        }

        return true;
    }
}