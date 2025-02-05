import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int N;
    static int[] dp;
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        dp = new int[N + 1];
        arr = new int[N + 1];
        Arrays.fill(dp, -1);
        Arrays.fill(arr, -1);

        if (recur(N)) {
            System.out.println(arr[N]);
        } else {
            System.out.println(-1);
        }



    }

    public static boolean recur(int cur) {
        if (cur == 10) {
            arr[cur] = 1;
            return true;
        }

        if (cur < 10) {
            return false;
        }

        if (dp[cur] != -1) {
            return dp[cur] == 1;
        }

        int cnt = 0;
        String str = String.valueOf(cur);
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < str.length(); i++) {
            for (int j = str.length() - 1; j >= i ; j--) {
                String substring = str.substring(i, j + 1);
                int num = Integer.parseInt(substring);

                if (num == 0 || num == cur) {
                    continue;
                }

                if (!recur(cur - num)) {
                    min = Math.min(min, num);
                    cnt++;
                }
            }
        }

        if (cnt > 0) {
            dp[cur] = 1;
            arr[cur] = min;
        } else {
            dp[cur] = 0;
        }

        return cnt > 0;
    }

}