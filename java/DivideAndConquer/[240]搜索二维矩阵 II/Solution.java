class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;

        int row = m - 1;
        int col = 0;

        while (col < n && row >= 0) {
            if (target == matrix[row][col]) return true;

            if (target < matrix[row][col]) {
                row--;
            } else col++;
        }

        return false;
        
    }
}