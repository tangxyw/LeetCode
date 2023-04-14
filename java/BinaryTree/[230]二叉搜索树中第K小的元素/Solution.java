import BinaryTree.TreeNode;

class Solution {
    int k;
    int res;

    public int kthSmallest(TreeNode root, int k) {
        this.k = k;
        inorder(root);

        return res;
    }

    private void inorder(TreeNode root) {
        if (root == null) return;

        inorder(root.left);
        if (--k == 0) {
            res = root.val;
            return;
        }
        inorder(root.right);
    }
}