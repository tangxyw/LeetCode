class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length;
        int p = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                if (i > p) {
                    int temp = nums[i];
                    nums[i] = nums[p];
                    nums[p] = temp;
                }
                p++;
            }
        }

        for (int j = p; j < n; j++) {
            if (nums[j] == 1) {
                if (j > p) {
                    int temp = nums[j];
                    nums[j] = nums[p];
                    nums[p] = temp;
                }
                p++;
            }
        }

    }
}