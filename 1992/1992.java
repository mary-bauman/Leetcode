class Solution {
    public void dfs(int row, int col, int m, int n, int[][] land){
        if (row < 0 || row >= m || col < 0 || col >= n || land[row][col] != 1) {return;}
        land[row][col] = 0;
        return;
    }
    public int[][] findFarmland(int[][] land) {
        int[][] result = new int[land.length*land[0].length][land.length*land[0].length];
        int ri = 0;
        int m = land.length;
        int n = land[0].length;

        for (int i = 0; i < land.length; i++){
            for (int j = 0; j < land[0].length; j++){
                if (land[i][j]==1){
                    int[] top_left = new int[]{i, j};
                    int[] bottom_right = new int[]{i,j};
                    dfs(i, j, m, n, land);
                    result[ri] = new int[]{top_left[0], top_left[1], bottom_right[0], bottom_right[1]};
                    ri+=1;}}}
        return result;}}
