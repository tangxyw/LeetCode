import BinaryTree.TreeNode;

class Solution {
    private int res = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        postorfer(root);
        
        return res;
    }

    private int postorfer(TreeNode root){
        if (root == null) return 0;

        int left = postorfer(root.left);
        int right = postorfer(root.right);

        int cur_res = Math.max(left, right) + 1;
        res = Math.max(res, left + right);

        return cur_res;
    }
}