import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] arr;
    static int[][] dpMax, dpMin;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());

        arr = new int[N][3];
        dpMax = new int[N][3];
        dpMin = new int[N][3];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            Arrays.fill(dpMax[i], -1);
            Arrays.fill(dpMin[i], -1);
        }

        int max = 0;
        int min = 1234567890;
        for (int i = 0; i < 3; i++) {
            max = Math.max(max, recurMax(0, i));
            min = Math.min(min, recurMin(0, i));
        }

        sb.append(max).append(" ").append(min);
        System.out.println(sb);

    }

    public static int recurMax(int depth, int idx) {
        if (depth == N) {
            return 0;
        }

        if (dpMax[depth][idx] != -1) {
            return dpMax[depth][idx];
        }

        int tmp = 0;
        for (int i = -1; i < 2; i++) {
            if (idx + i < 0 || idx + i > 2) {
                continue;
            }
            tmp = Math.max(tmp, recurMax(depth + 1, idx + i) + arr[depth][idx + i]);
        }

        return dpMax[depth][idx] = tmp;
    }

    public static int recurMin(int depth, int idx) {
        if (depth == N) {
            return 0;
        }

        if (dpMin[depth][idx] != -1) {
            return dpMin[depth][idx];
        }

        int tmp = 1234567890;
        for (int i = -1; i < 2; i++) {
            if (idx + i < 0 || idx + i > 2) {
                continue;
            }
            tmp = Math.min(tmp, recurMin(depth + 1, idx + i) + arr[depth][idx + i]);
        }

        return dpMin[depth][idx] = tmp;
    }

}