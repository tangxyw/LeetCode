class Solution {
    public int maxProfit(int[] prices) {
        int max_bonus = 0;
        int min_price = prices[0];

        for (int i = 1; i < prices.length; i++) {
            max_bonus = Math.max(max_bonus, prices[i] - min_price);
            min_price = Math.min(min_price, prices[i]);
        }

        return max_bonus;

    }
}