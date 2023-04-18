class Solution {
    int cur_area = 0;
    int max_area = 0;
    int[][] grid;
    int m, n;

    public int maxAreaOfIsland(int[][] grid) {
        this.grid = grid;
        this.m = grid.length;
        this.n = grid[0].length;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    cur_area = 0;
                    dfs(i, j);
                    max_area = Math.max(max_area, cur_area);
                }
            }
        }

        return max_area;
    }

    private void dfs(int x, int y) {
        if (x < 0 || x >= m || y < 0 || y >= n) return;

        if (grid[x][y] == 0) return;

        grid[x][y] = 0;
        cur_area++;
        dfs(x - 1, y);
        dfs(x + 1, y);
        dfs(x, y - 1);
        dfs(x, y + 1);
    }
}