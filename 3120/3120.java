class Solution {
    public int numberOfSpecialChars(String word) {
        Set<Character> lowercase = new HashSet<>();

        for (int i = 0; i < word.length(); i++) {
            if (Character.isLowerCase(word.charAt(i)) && word.contains(Character.toUpperCase(word.charAt(i)) + "")) {
                lowercase.add(word.charAt(i));}}
        return lowercase.size();}}
