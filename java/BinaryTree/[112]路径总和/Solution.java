import BinaryTree.TreeNode;

class Solution {
    private boolean res = false; 

    public boolean hasPathSum(TreeNode root, int targetSum) {
        dfs(root, targetSum);
        
        return res;
    }

    private void dfs(TreeNode root, int targetSum) {
        if (res) return;
        
        if (root == null) return;

        if (root.left == null && root.right == null && root.val == targetSum) {
            res = true;
            return;
        }

        TreeNode[] nodes = {root.left, root.right};

        for (TreeNode node: nodes) {
            dfs(node, targetSum - root.val);
        }
    }
}