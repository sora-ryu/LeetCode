class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int answer[] = new int[2];
        int first = 0;
        int second = 0;
        
        for (int i=0; i<nums.length; i++) {
            int temp = nums[i];
            for (int j=0; j<nums.length; j++) {
                if (j == i) continue;
                if (target - temp == nums[j]) {
                    first = i;
                    second = j;
                }
            }
        }
        
        answer[0] = first;
        answer[1] = second;
        
        return answer;
    }
}