class Solution {
    private boolean[][] used;
    private int m, n;
    private char[][] board;
    private char[] word;
    private int[][] direction = new int[][] {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

    public boolean exist(char[][] board, String word) {
        this.board = board;
        this.m = board.length;
        this.n = board[0].length;
        this.used = new boolean[m][n];
        this.word = word.toCharArray();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dfs(i, j, 0) == true) return true;
            }
        }

        return false;
    }

    private boolean dfs(int x, int y, int index) {
        if (board[x][y] != word[index]) return false;
        if (index == word.length - 1) return true;

        used[x][y] = true;
        for (int[] d : direction) {
            int nx = x + d[0];
            int ny = y + d[1];
            if (nx >= 0 && nx < m && ny >= 0 && ny < n && !used[nx][ny] && dfs(nx, ny, index+1)) {
                return true;
            }
        }
        used[x][y] = false;

        return false;
    } 
}