import java.BinaryTree.TreeNode;

class Solution {
    private int[] nums;

    public TreeNode sortedArrayToBST(int[] nums) {
        this.nums = nums;
        return sortedArrayToBST(0, nums.length-1);

    }

    private TreeNode sortedArrayToBST(int start, int end) {
        if (start > end) return null;

        int mid = start + (end - start) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = sortedArrayToBST(start, mid-1);
        node.right = sortedArrayToBST(mid+1, end);

        return node;
    }
}