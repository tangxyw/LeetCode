import BinaryTree.TreeNode;

class Solution {
    public boolean isBalanced(TreeNode root) {
        int res = postorder(root);

        return res == -1 ? false : true;
    }

    private int postorder(TreeNode root) {
        if (root == null) return 0;

        int left = postorder(root.left);
        int right = postorder(root.right);

        if (left == -1 || right == -1 || Math.abs(left-right) > 1) return -1;

        return Math.max(left, right) + 1;
    }
}