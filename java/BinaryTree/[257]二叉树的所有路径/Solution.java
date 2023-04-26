import java.util.ArrayList;
import java.util.List;
import BinaryTree.TreeNode;

class Solution {
    private List<String> res = new ArrayList<String>();

    public List<String> binaryTreePaths(TreeNode root) {
        dfs(root, "");
        
        return res;
    }

    private void dfs(TreeNode root, String path) {
        if (root == null) {
            return;
        }

        path += root.val;
        if (root.left == null && root.right == null) {
            res.add(path);
            return;
        }

        dfs(root.left, path+"->");
        dfs(root.right, path+"->");

    } 
}