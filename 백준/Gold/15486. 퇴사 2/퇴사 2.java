import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] arr;
    static int[] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();


        N = Integer.parseInt(br.readLine());
        arr = new int[N][2];
        dp = new int[N + 1];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        dp[N] = 0;
        for (int i = N - 1; i >= 0; i--) {
            if (i + arr[i][0] < N + 1) {
                dp[i] = Math.max(dp[i + 1], dp[i + arr[i][0]] + arr[i][1]);
            } else {
                dp[i] = dp[i + 1];
            }
        }
        System.out.println(dp[0]);
    }

    public static int recur(int time) {
        if (time > N) {
            return -99999999;
        }

        if (time == N) {
            return 0;
        }

        if (dp[time] != -1) {
            return dp[time];
        }


        return dp[time] = Math.max(recur(time + 1), recur(time + arr[time][0]) + arr[time][1]);
    }


}