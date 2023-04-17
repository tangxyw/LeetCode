class Solution {
    public int findDuplicate(int[] nums) {
        int slow = 0, fast = 0;
        while (true) {
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast) break;
        }

        int p = 0;
        while (p != slow) {
            p = nums[p];
            slow = nums[slow];
        }

        return p;
    }
}