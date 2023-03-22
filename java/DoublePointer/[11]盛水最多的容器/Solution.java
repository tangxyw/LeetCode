class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int max_area = 0;
        int cur_area = 0;
        while (left < right) {
            cur_area = (right - left) * Math.min(height[left], height[right]);
            max_area = Math.max(max_area, cur_area);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return max_area;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int result = solution.maxArea(new int[] {1,8,6,2,5,4,8,3,7});
        System.out.println(result);
    }
}
