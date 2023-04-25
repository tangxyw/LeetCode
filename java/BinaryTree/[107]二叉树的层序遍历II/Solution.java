import java.util.List;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Queue;
import BinaryTree.TreeNode;

class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        Queue<TreeNode> q = new LinkedList<>();

        if (root == null) return res;

        q.add(root);

        while (!q.isEmpty()) {
            List<Integer> layer_res = new ArrayList<>();
            int size = q.size(); 
            for (int i = 0; i < size; i++) {
                TreeNode node = q.poll();
                layer_res.add(node.val);
                if (node.left != null) {
                    q.offer(node.left);
                }
                if (node.right != null) {
                    q.offer(node.right);
                }
            }
            res.add(0, layer_res);            
        }

        return res;
    }
}