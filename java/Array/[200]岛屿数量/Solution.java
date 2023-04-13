class Solution {
    private int m;
    private int n;
    private char[][] grid; 

    public int numIslands(char[][] grid) {
        this.m = grid.length;
        this.n = grid[0].length;
        this.grid = grid;

        int res = 0;

        for (int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    res++;
                    dfs(i,j);
                }
            }
        }

        return res;
    }

    private void dfs (int x, int y) {
        if (x < 0 || x >= m || y < 0 || y >= n) return;

        if (grid[x][y] == '0') return;

        grid[x][y] = '0';

        dfs(x-1, y);
        dfs(x+1, y);
        dfs(x, y-1);
        dfs(x, y+1);
    }
}