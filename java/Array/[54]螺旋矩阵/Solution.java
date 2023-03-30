import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int rest_nums = matrix.length * matrix[0].length;
        List<Integer> res = new ArrayList<>();

        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;

        while (rest_nums >= 1) {
            // 左到右
            for (int j = left; j <= right; j++) {
                if (rest_nums >= 1) {
                    res.add(matrix[top][j]);
                    rest_nums--;
                }
            }
            top++;

            // 上到下
            for (int i = top; i <= bottom; i++) {
                if (rest_nums >= 1) {
                    res.add(matrix[i][right]);
                    rest_nums--;
                }
            }
            right--;

            // 右到左
            for (int j = right; j >= left; j--) {
                if (rest_nums >= 1) {
                    res.add(matrix[bottom][j]);
                    rest_nums--;
                }
            }
            bottom--;

            // 下到上
            for (int i = bottom; i >= top; i--) {
                if (rest_nums >= 1) {
                    res.add(matrix[i][left]);
                    rest_nums--;
                }
            }
            left++;
        } 

        return res;
    }
}