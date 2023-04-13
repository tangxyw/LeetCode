class Solution {
    public boolean isHappy(int n) {
        int slow = n, fast = n;

        while (true) {
            slow = getNextNum(slow);
            fast = getNextNum(getNextNum(fast));
            if (slow == 1 || fast == 1) return true;
            if (slow == fast) return false;
        }
    }

    private int getNextNum(int n) {
        int sum = 0;
        while (n > 0) {
            int x = n % 10;
            sum += x * x;
            n /= 10; 
        }

        return sum;
    }
}