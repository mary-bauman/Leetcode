class Solution {
    public String shortestPalindrome(String s) {
        int n = s.length();
        String rs = new StringBuilder(s).reverse().toString();
        for(int i = 0; i < n; i++){
            if (s.substring(0,(n-i)).equals(rs.substring(i))){
                return rs.substring(0,i) + s;
            }
        }
        return "";
    }
}
