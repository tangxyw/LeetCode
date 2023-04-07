import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();

        for(int i = 0; i < numRows; i++) {
            List<Integer> layer_res = new ArrayList<Integer>();
            for(int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    layer_res.add(1);
                } else {
                    layer_res.add(res.get(i - 1).get(j - 1) + res.get(i - 1).get(j));
                }
            }
            res.add(layer_res);
        }
        return res;
    }

    public static void main(String[] args) {
        List<List<Integer>> res = new Solution().generate(6);
        System.out.print(res);
    }
}