class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int top = 0, bottom = matrix.length - 1;

        while (top <= bottom) {
            int mid = top + (bottom - top) / 2;
            if (target < matrix[mid][0]) bottom = mid - 1;
            else if (target == matrix[mid][0]) return true;
            else top = mid + 1; 
        }

        int left = 0, right = matrix[0].length - 1;
        int row = bottom;

        if (row < 0) return false;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (target < matrix[row][mid]) right = mid - 1;
            else if (target == matrix[row][mid]) return true;
            else left = mid + 1;
        }

        return false;

    }
}