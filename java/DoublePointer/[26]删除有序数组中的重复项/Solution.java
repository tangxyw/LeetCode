class Solution {
    public int removeDuplicates(int[] nums) {
        int left = 0, right = 1;

        while (right < nums.length) {
            if (nums[left] == nums[right]) {
                right++;
            } else {
                nums[left+1] = nums[right];
                left++;
                right++;
            }
        }
        return left + 1;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.removeDuplicates(new int[] {1,2,2,3,3,4});
        System.out.println(result);
    }
}
