class Solution {
    public int minOperations(int[][] grid, int x) {
        int result = 0;
        //create a
        int n = grid.length * grid[0].length;
        int[] a = new int[n];
        int index = 0;
        for (int[] row : grid) {
            for (int num : row) {
                a[index++] = num;
            }
        }
        Arrays.sort(a);
        int common = a[Math.floorDiv(n,2)];
        int commonX = common % x;
        for (int num : a){
            if (num%x != commonX) return -1;
            result += Math.floorDiv(Math.abs(common-num), x);
        }


        return result;
    }
}
