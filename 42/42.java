class Solution {
    public int trap(int[] height) {
        int sm = 0;
        int n = height.length;
        int[] pre = new int[n];
        int[] suf = new int[n];

        pre[0] = height[0];
    
        for (int i = 1; i < n; i++){
            pre[i] = Math.max(pre[i-1],height[i]);}

        suf[n-1] = height[n-1];

        for (int i = n - 2; i >= 0; i--){
            suf[i] = Math.max(suf[i+1],height[i]);}

        for (int i = 0; i < n; i++){
            sm += Math.min(suf[i],pre[i])  - height[i];}
    
        return sm;}}
