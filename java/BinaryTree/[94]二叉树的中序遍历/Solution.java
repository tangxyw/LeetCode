import java.BinaryTree.TreeNode;
import java.util.ArrayList;
import java.util.List;

class Solution {
    private List<Integer> res = new ArrayList<Integer>();

    public List<Integer> inorderTraversal(TreeNode root) {
        inorder(root);
        return res;
    }

    private void inorder(TreeNode root) {
        if (root == null) return;

        inorder(root.left);
        res.add(root.val);
        inorder(root.right);
    }
}