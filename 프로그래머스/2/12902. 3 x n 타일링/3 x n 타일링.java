class Solution {
    public long solution(int n) {
        if(n % 2 == 1) return 0;
        
        long[] dp = new long[n + 1];
        dp[0] = 1;
        dp[2] = 3;
        for(int i = 4; i <= n; i += 2){
            dp[i] = 3 * dp[i - 2];
            for(int j = i - 4; j >= 0; j -= 2) {
                dp[i] += dp[j] * 2;
            }
            dp[i] %= 1000000007;
        }
        return dp[n];
    }
}
