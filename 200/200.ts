function numIslands(grid: string[][]): number {
    if (grid.length==0){
        return 0;}
    function dfs(i: number, j: number): void{
        if (i < 0 || j<0 || i >= grid.length || j >= grid.length || (grid[i][j]!=='1')){
            return;}
        grid[i][j] = '0';
        dfs(i-1,j);
        dfs(i+1,j);
        dfs(i,j-1);
        dfs(i,j+1);}
    var num_islands: number = 0;
    for (var i: number = 0; i < grid.length; i++){
        for (var j: number = 0; j < grid[0].length; j++){
            if (grid[i][j]=='1'){
                num_islands+=1;
                dfs(i,j);}}}
    return num_islands;
};
