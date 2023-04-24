import BinaryTree.TreeNode;

class Solution {
    private int[] inorder;
    private int[] postorder;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        this.inorder = inorder;
        this.postorder = postorder;

        TreeNode root = buildTree(0, inorder.length - 1, 0, postorder.length - 1);

        return root;
    }

    private TreeNode buildTree(int inorder_start, int inorder_end, int postorder_start, int postorder_end) {
        if (inorder_start > inorder_end) return null;
        
        int value = postorder[postorder_end];
        TreeNode root = new TreeNode(value);

        int index = findIndex(value, inorder, inorder_start, inorder_end);

        // 左子树
        int left_inorder_start = inorder_start;
        int left_inorder_end =  index - 1;
        int left_postorder_start = postorder_start;
        int left_postorder_end = postorder_start + index - inorder_start - 1;

        // 右子树
        int right_inorder_start = index + 1;
        int right_inorder_end = inorder_end;
        int right_postorder_start = left_postorder_end + 1;
        int right_postorder_end = right_postorder_start + inorder_end - index - 1;

        root.left = buildTree(left_inorder_start, left_inorder_end, left_postorder_start, left_postorder_end);
        root.right = buildTree(right_inorder_start, right_inorder_end, right_postorder_start, right_postorder_end);
        
        return root;
    }

    private int findIndex(int val, int[] inorder, int start, int end) {
        int i = start;
        for (; i <= end; i++) {
            if (inorder[i] == val) break;
        }
        return i;
    }
}