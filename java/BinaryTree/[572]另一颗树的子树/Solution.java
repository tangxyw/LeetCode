import BinaryTree.TreeNode;

class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) return true;
        if (root == null || subRoot == null) return false;

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot) || isSametree(root, subRoot);

    }

    private boolean isSametree(TreeNode root1, TreeNode root2) {
        if (root1 == null && root2 == null) return true;
        if (root1 == null || root2 == null) return false;

        return root1.val == root2.val && isSametree(root1.left, root2.left) && isSametree(root1.right, root2.right);
    }
}