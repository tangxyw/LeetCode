class Solution {
    public int search(int[] nums, int target) {
        return helper(0, nums.length - 1, nums, target);
    }

    private int helper(int start, int end, int[] nums, int target) {
        if (start == end) {
            if (nums[start] == target) return start;
            return -1;
        }

        if (nums[start] < nums[end] && (nums[start] > target || nums[end] < target)) return -1;
        int mid = start + (end - start) / 2;
        return Math.max(helper(start, mid, nums, target), helper(mid+1, end, nums, target));
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.search(new int[] {4,5,6,7,0,1,2}, 1);
        System.out.println(result);
    }
}
