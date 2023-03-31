import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] interval1, int[] interval2) {
                return interval1[0] - interval2[0];
            }
        });

        List<int[]> res = new ArrayList<>();

        for (int i = 0; i < intervals.length; i++) {
            if (res.isEmpty() || res.get(res.size()-1)[1] < intervals[i][0]) {
                res.add(intervals[i]);
            } else {
                res.get(res.size()-1)[1] = Math.max(res.get(res.size()-1)[1], intervals[i][1]);
            }
        }

        return res.toArray(new int[res.size()][2]);
    }
}