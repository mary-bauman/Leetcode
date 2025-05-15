class Solution {
    public int minimumDeletions(String s) {
        int bCount = 0;
        int deletionCount = 0;
        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i)=='a') deletionCount = Math.min(deletionCount+1, bCount);
            else bCount++;
        }
        return deletionCount;
    }
}
