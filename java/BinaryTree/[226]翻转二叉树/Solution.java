import BinaryTree.TreeNode;

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;

        TreeNode temp = new TreeNode(0);
        temp = root.left;
        root.left = root.right;
        root.right = temp;

        root.left = invertTree(root.left);
        root.right = invertTree(root.right);

        return root; 


    }
}