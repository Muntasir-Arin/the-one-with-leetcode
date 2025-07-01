class Solution {
    public int possibleStringCount(String word) {
        
        int len = word.length();
        
        for (int i=1; i<word.length(); i++){
            if (word.charAt(i)!=word.charAt(i-1)){
                len --;
            }
        }

        return len;
    }
}