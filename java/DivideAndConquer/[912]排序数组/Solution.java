import java.util.Random;

class Solution {
    public int[] sortArray(int[] nums) {
        quicksort(nums, 0, nums.length-1);
        
        return nums;
    }

    private void quicksort(int[] nums, int start, int end) {
        if (start >= end) return;

        int t = new Random().nextInt(end - start + 1) + start;
        int pivot = nums[t];
        swap(nums, start, t);

        int i = start;
        int j = end;

        while (i < j) {
            while(i < j && nums[j] >= pivot) j--;
            while(i < j && nums[i] <= pivot) i++;
            swap(nums, i, j);
        }
        swap(nums, start, i);

        quicksort(nums, start, i-1);
        quicksort(nums, i+1, end);

        return;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
        
        return;
    }
}