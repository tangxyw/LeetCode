import BinaryTree.TreeNode;

class Solution {
    public int sumNumbers(TreeNode root) {
        return postorfer(root, 0);
    }

    private int postorfer(TreeNode root, int value) {
        if (root == null) return 0;

        int cur_value = value * 10 + root.val;
        if (root.left == null && root.right == null) return cur_value;

        int left = postorfer(root.left, cur_value);
        int right = postorfer(root.right, cur_value);

        return left + right;
    }
}