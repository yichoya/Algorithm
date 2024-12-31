import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static int[] arr;
    static int[][][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        dp = new int[N][2501][2501];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < 2501; j++) {
                Arrays.fill(dp[i][j], -1);
            }
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            K += arr[i];
        }

        System.out.println(recur(0, 0, 0));

    }

    public static int recur(int cur, int A, int B) {
        if (cur == N) {
            if (K - (A + B) > A || K - (A + B) > B) {
                return -123456789;
            }
            return 0;
        }

        if (dp[cur][A][B] != -1) {
            return dp[cur][A][B];
        }

        int tmp = -123456789;

        tmp = Math.max(tmp, recur(cur + 1, A + arr[cur], B));
        tmp = Math.max(tmp, recur(cur + 1, A, B + arr[cur]));
        tmp = Math.max(tmp, recur(cur + 1, A, B) + arr[cur]);

        return dp[cur][A][B] = tmp;
    }

}