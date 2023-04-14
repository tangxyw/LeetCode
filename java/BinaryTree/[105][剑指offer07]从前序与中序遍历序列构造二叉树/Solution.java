import BinaryTree.TreeNode;

class Solution {
    private int[] preorder;
    private int[] inorder;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        this.preorder = preorder;
        this.inorder = inorder;
        return buildTree(0, preorder.length - 1, 0, inorder.length - 1);
    }

    private TreeNode buildTree(int preorder_start, int preorder_end, int inorder_start, int inorder_end) {
        if (preorder_start > preorder_end) return null;

        int root_val = preorder[preorder_start];
        int index = findIndex(root_val, inorder, inorder_start, inorder_end);
        // 左子树节点数
        int l_node_num = index - inorder_start;

        // 左子树4个参数
        int l_preorder_start = preorder_start + 1;
        int l_preorder_end = preorder_start + l_node_num;
        int l_inorder_start = inorder_start;
        int l_inorder_end = index - 1;

        // 右子树4个参数
        int r_preorder_start = l_preorder_end + 1;
        int r_preorder_end = preorder_end;
        int r_inorder_start = index + 1;
        int r_inorder_end = inorder_end;

        TreeNode node = new TreeNode(root_val);
        node.left = buildTree(l_preorder_start, l_preorder_end, l_inorder_start, l_inorder_end);
        node.right = buildTree(r_preorder_start, r_preorder_end, r_inorder_start, r_inorder_end);

        return node;
    }

    private int findIndex(int val, int[] inorder, int start, int end) {
        int i = start;
        for (; i <= end; i++) {
            if (inorder[i] == val) break;
        }
        return i;
    }
}