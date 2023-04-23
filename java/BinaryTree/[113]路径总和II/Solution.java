import java.util.ArrayList;
import java.util.List;
import BinaryTree.TreeNode;

class Solution {
    private List<List<Integer>> res = new ArrayList<>();

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<Integer> track = new ArrayList<>();

        traceback(root, targetSum, track);

        return res;
    }

    private void traceback(TreeNode root, int targetSum, List<Integer> track) {
        if (root == null) return;

        track.add(root.val);
        
        if (root.left == null && root.right == null && root.val == targetSum) {
            res.add(new ArrayList<>(track));
        }

        TreeNode[] childs = new TreeNode[] {root.left, root.right};
        for (TreeNode node: childs) {
            traceback(node, targetSum - root.val, track);
        }                    
        track.remove(track.size() - 1);

    }
}