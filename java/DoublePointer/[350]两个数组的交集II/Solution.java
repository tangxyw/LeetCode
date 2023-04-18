import java.util.Arrays;

class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        int p1 = 0, p2 = 0;
        int n1 = nums1.length, n2 = nums2.length;

        int[] res = new int[Math.min(n1, n2)];
        int index = 0;    
        while(p1 < n1 && p2 < n2) {
            if (nums1[p1] == nums2[p2]) {
                res[index] = nums1[p1];
                index++;
                p1++;
                p2++;
            } else if (nums1[p1] > nums2[p2]) p2++;
            else p1++;
        }

        return Arrays.copyOfRange(res, 0, index);
    }
}