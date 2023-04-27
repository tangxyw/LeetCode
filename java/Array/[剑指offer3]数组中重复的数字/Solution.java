class Solution {
    public int findRepeatNumber(int[] nums) {
        int n = nums.length;
        int i = 0;

        while (i < n) {
            if (nums[i] == i) {
                i++;
                continue;
            }
            int j = nums[i];
            if (nums[i] == nums[j]) return nums[i];
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }

        return -1;
    }
}