class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int n = s.length();
        int start = 0;
        int curCost = 0;
        int maxLen = 0;
        int lenMin = Math.min(s.length(),t.length());
        
        for (int end = 0; end < n; end++){
            curCost += Math.abs(((int) s.charAt(end)) - ((int) t.charAt(end)));
            while (curCost > maxCost){
                curCost -= Math.abs((int) (s.charAt(start)) - ((int) t.charAt(start)));
                start += 1;}
            maxLen = Math.max(maxLen, (end-start+1));}
        return maxLen;}}
