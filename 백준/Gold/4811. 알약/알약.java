import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int N;
    static int[] arr;
    static long[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        while (true) {
            N = Integer.parseInt(br.readLine());

            if (N == 0) {
                break;
            }
            arr = new int[2];
            arr[0] = N - 1;
            arr[1] = 1;
            dp = new long[N + 1][N + 1];

            for (int i = 0; i < N + 1; i++) {
                Arrays.fill(dp[i], -1);
            }

            System.out.println(recur(1, 0));
        }
        System.out.println(sb);

    }

    public static long recur(int one, int half) {
        if (one + half > 2 * N) {
            return 0;
        }

        if (one + half == 2 * N) {
            return 1;
        }

        if (dp[one][half] != -1) {
            return dp[one][half];
        }

        long tmp = 0;
        if (arr[0] > 0) {
            arr[0] -= 1;
            arr[1] += 1;
            tmp += recur(one + 1, half);
            arr[0] += 1;
            arr[1] -= 1;
        }
        if (arr[1] > 0) {
            arr[1] -= 1;
            tmp += recur(one, half + 1);
            arr[1] += 1;
        }

        return dp[one][half] = tmp;
    }


}