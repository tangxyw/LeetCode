import java.util.HashMap;
import java.util.Map;

class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> pre_count = new HashMap<Integer, Integer>();
        pre_count.put(0, 1);
        int pre = 0;
        int res = 0;

        for (int num : nums) {
            pre += num;
            if (pre_count.containsKey(pre-k)) res += pre_count.get(pre-k);
            pre_count.put(pre, pre_count.getOrDefault(pre, 0) + 1);
        }

        return res;
    }
}