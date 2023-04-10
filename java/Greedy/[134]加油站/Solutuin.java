class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int n = gas.length;
        int i = 0;

        while (i < n) {
            int j = i;
            int remain = gas[i];

            while (remain - cost[j] >= 0) {
                remain += gas[(j+1) % n] - cost[j];
                j = (j+1) % n;
                if (j == i) return i;
            }
            if (j < i) return -1;
            i = j + 1;
        }

        return -1;

    }
}