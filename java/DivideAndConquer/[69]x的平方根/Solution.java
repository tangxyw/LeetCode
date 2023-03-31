class Solution {
    public int mySqrt(int x) {
        if (x == 0 || x == 1) return x;
        
        int left = 1, right = x / 2;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (mid <= x/mid && mid+1 > x / (mid+1)) return mid;
            if (mid > x/mid) right = mid - 1;
            else left = mid + 1;
        }

        return 0;
    }
}