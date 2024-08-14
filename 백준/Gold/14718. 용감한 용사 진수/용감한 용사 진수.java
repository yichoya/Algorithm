import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] arr = new int[N][3];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int STR = Integer.parseInt(st.nextToken());
            int DEX = Integer.parseInt(st.nextToken());
            int INT = Integer.parseInt(st.nextToken());

            arr[i][0] = STR;
            arr[i][1] = DEX;
            arr[i][2] = INT;
        }
        int answer = 3_000_000;

        // 모든 경우의 수를 검사
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    int cnt = 0;

                    // N명의 병사를 순환하면서 이길 수 있는 병사 수 확인
                    for (int l = 0; l < N; l++) {
                        if (arr[i][0] >= arr[l][0] && arr[j][1] >= arr[l][1] && arr[k][2] >= arr[l][2]) {
                            cnt++;
                        }
                    }

                    if (cnt >= K) {
                        answer = Math.min(answer, arr[i][0] + arr[j][1] + arr[k][2]);
                    }
                }
            }
        }
        System.out.println(answer);
    }

}

/*
3 2
234 23 342
35 4634 34
46334 6 789
 */