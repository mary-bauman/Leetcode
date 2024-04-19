class Solution {
    char[][] grid;
    public void dfs(int i, int j){
        if ((i<0) || (i>=grid.length) || (j < 0) || (j >= grid[0].length) || (grid[i][j]!='1')){
            return;}
        grid[i][j] = '0';  // mark as visited
        dfs(i+1, j);
        dfs(i-1, j);
        dfs(i, j+1);
        dfs(i, j-1);
        return;}
    public int numIslands(char[][] g) {
        grid = g;
        if (grid.length==0) return 0;
        int num_islands = 0;
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j]=='1'){
                    num_islands += 1;
                    dfs(i,j);}}}
        return num_islands;}}
