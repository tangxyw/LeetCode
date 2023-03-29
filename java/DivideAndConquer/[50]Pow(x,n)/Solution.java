class Solution {
    public double myPow(double x, int n) {
        long N = n;
        return myPow2(x, N);
    }

    private double myPow2(double x, long n) {
        if (n == 0) return 1;
        if (n == 1) return x;

        if (n < 0) return 1.0 / myPow2(x, -n);

        double y = myPow2(x, n/2);
        if (n % 2 == 0) {
            return y * y;
        } else {
            return y * y * x;
        } 
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        double result = solution.myPow(2.0, 10);
        System.out.println(result);
    }
}