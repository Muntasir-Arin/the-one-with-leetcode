class Solution {
    public int maximumPossibleSize(int[] nums) {
        int output = 0;
        int currentMax = Integer.MIN_VALUE;

        for (int num : nums) {
            if (num >= currentMax) {
                output++;
                currentMax = num;
            }
        }

        return output;
    }
}
