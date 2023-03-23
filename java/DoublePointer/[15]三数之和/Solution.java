import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        int n = nums.length;

        Arrays.sort(nums);

        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                break;
            }
            if (i > 0 && nums[i-1] == nums[i]) {
                continue;
            }

            int left = i + 1;
            int right = n - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    while (left < right && nums[left] == nums[left+1]) {
                        left++;
                    }
                    while (left < right && nums[right] == nums[right-1]) {
                        right--;
                    }
                    left++;
                    right--;
                } else if (sum < 0) {
                    while (left < right && nums[left] == nums[left+1]) {
                        left++;
                    }
                    left++;
                } else if (sum > 0) {
                    while (left < right && nums[right] == nums[right-1]) {
                        right--;
                    }
                    right--;
                }
            }
        }
        return res;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        List<List<Integer>> result = solution.threeSum(new int[] {-1,0,1,2,-1,-4});
        System.out.println(result);
    }
}