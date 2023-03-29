class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[][] row = new int[9][9];
        int[][] col = new int[9][9];
        int[][] box = new int[9][9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int num = Character.getNumericValue(board[i][j]);

                    if (row[i][num-1] > 0) {
                        return false;
                    } else row[i][num-1] = 1;

                    if (col[j][num-1] > 0) {
                        return false;
                    } else col[j][num-1] = 1;

                    if (box[(i / 3) * 3 + j / 3][num-1] > 0) {
                        return false;
                    } else box[(i / 3) * 3 + j / 3][num-1] = 1;
                }
            }
        }

        return true;
    }
}