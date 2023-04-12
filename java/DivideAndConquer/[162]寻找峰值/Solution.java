class Solution {
    int[] nums;

    public int findPeakElement(int[] nums) {
        this.nums = nums;
        int left = 0, right = nums.length - 1;

        while (left <= right) {
            if (left == right) return left;

            int mid = left + (right - left ) / 2;
            if (get(mid) > Math.max(get(mid-1), get(mid+1))) return mid;
            else if (get(mid) < get(mid+1)) left = mid + 1;
            else right = mid - 1; 
        }

        return -1;
    }

    private int get(int i) {
        if (i == -1 || i == nums.length) return Integer.MIN_VALUE;
        
        return nums[i];
    }
}