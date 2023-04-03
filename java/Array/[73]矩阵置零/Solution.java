class Solution {
    public void setZeroes(int[][] matrix) {
        boolean row_flag = false, col_flag = false;

        int m = matrix.length, n = matrix[0].length;

        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                col_flag = true;
                break;
            }
        }

        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                row_flag = true;
                break;
            }
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        if (col_flag == true) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }

        if (row_flag == true) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }

    }
}