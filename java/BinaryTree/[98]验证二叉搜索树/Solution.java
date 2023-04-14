import BinaryTree.TreeNode;

class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }

    public boolean isValidBST(TreeNode root, long lower, long upper) {
        if (root == null) return true;

        if (root.val >= upper || root.val <= lower) return false;

        return isValidBST(root.left, lower, root.val) && isValidBST(root.right, root.val, upper);
    }
}