import java.util.HashSet;
import java.util.Set;

class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> num_set = new HashSet<Integer>();
        int longest_streak = 0;
        
        for (int num : nums) {
            num_set.add(num);
        }

        for (int num : num_set) {
            if (!num_set.contains(num-1)) {
                int current_num = num;
                int current_streak = 1;
                while (num_set.contains(current_num+1)) {
                    current_num++;
                    current_streak++;
                }
                longest_streak = Math.max(longest_streak, current_streak);
            }
        }

        return longest_streak;
    }
}