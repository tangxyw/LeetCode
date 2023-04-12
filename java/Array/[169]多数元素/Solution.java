class Solution {
    public int majorityElement(int[] nums) {
        int counter = 0;
        int cur_num = nums[0];
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            if (nums[i] == cur_num) {
                counter++;
            } else if (counter == 0) cur_num = nums[i];
            else counter--;
        }

        return cur_num;
    }
}