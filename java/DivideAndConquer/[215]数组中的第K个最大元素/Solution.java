import java.util.Random;

class Solution {
    int[] nums;
    int k;

    public int findKthLargest(int[] nums, int k) {
        this.nums = nums;
        this.k = k;

        quicksort(0, nums.length - 1);

        return nums[k-1];
    }

    private void quicksort(int start, int end) {
        if (start == end) return;

        int t = new Random().nextInt(end - start + 1) + start;
        int pivot = nums[t];
        swap(start, t);

        int i = start, j = end;
        while (i < j) {
            while (i < j && nums[j] <= pivot) j--;
            while (i < j && nums[i] >= pivot) i++;
            swap(i, j);
        }
        swap(start, i);

        if (k - 1 == i) return;
        if (k - 1 < i) quicksort(start, i - 1);
        if (k - 1 > i) quicksort(i + 1, end);
    }

    private void swap(int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    } 
}