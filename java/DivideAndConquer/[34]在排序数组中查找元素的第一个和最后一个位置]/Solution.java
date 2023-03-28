import java.util.Arrays;

class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums.length  == 0) return new int[] {-1, -1};

        return helper(0, nums.length - 1, nums, target);
    }

    private int[] helper(int left, int right, int[] nums, int target) {
        if (nums[left] == nums[right] && nums[right] == target) return new int[] {left, right};
        if (target < nums[left] || target > nums[right]) return new int[] {-1, -1};

        int mid = left + (right - left) / 2;
        int[] l = helper(left, mid, nums, target);
        int[] r = helper(mid+1, right, nums, target);

        if (l[0] == -1 || r[0] == -1) {
            return l[0] == -1 ? r : l;        
        }
        return new int[] {l[0], r[1]};
  
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] result = solution.searchRange(new int[] {5,7,7,8,8,10}, 8);
        System.out.println(Arrays.toString(result));
    }
}