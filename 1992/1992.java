class Solution {
    public int[] top_left = new int[]{0, 0};
    public int[] bottom_right = new int[]{0,0};
    public int m = 0;
    public int n = 0;
    public void dfs(int row, int col, int[][] land){
        if (row < 0 || row >= m || col < 0 || col >= n || land[row][col] != 1) {return;}
        land[row][col] = 0;
        //Expand the boundaries of the current group
        top_left[0] = Math.min(top_left[0], row);
        top_left[1] = Math.min(top_left[1], col);
        bottom_right[0] = Math.max(bottom_right[0], row);
        bottom_right[1] = Math.max(bottom_right[1], col);
        
        //Perform DFS in all four directions
        dfs(row + 1, col, land);
        dfs(row - 1, col, land);
        dfs(row, col + 1, land);
        dfs(row, col - 1, land);
    }
    public int[][] findFarmland(int[][] land) {
        int[][] result = new int[land.length*land[0].length][land.length*land[0].length];
        int ri = 0;
        m = land.length;
        n = land[0].length;

        for (int i = 0; i < land.length; i++){
            for (int j = 0; j < land[0].length; j++){
                if (land[i][j]==1){
                    top_left = new int[]{i, j};
                    bottom_right = new int[]{i,j};
                    dfs(i, j, land);
                    result[ri] = new int[]{top_left[0], top_left[1], bottom_right[0], bottom_right[1]};
                    ri+=1;}}}
        return Arrays.copyOfRange(result,0,ri);}}
