import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    static int[][] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        arr = new int[N][3];
        long s= 1;
        long e = 0;
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
            arr[i][2] = Integer.parseInt(st.nextToken());

            e = Math.max(e, arr[i][1]);
        }

        long num = -1;
        while (s <= e) {
            long mid = s + (e - s) / 2;

            long tmp = calc(mid);
            if (tmp % 2 != 0) {
                e = mid - 1;
                num = mid;
            } else {
                s = mid + 1;
            }
        }

        if (num != -1) {
            sb.append(num).append(" ");

            int cnt = 0;
            for (int i = 0; i < N; i++) {
                if (arr[i][0] > num || arr[i][1] < num) {
                    continue;
                }

                if ((num - arr[i][0]) % arr[i][2] == 0) {
                    cnt++;
                }
            }
            sb.append(cnt);
        } else {
            sb.append("NOTHING");
        }
        System.out.println(sb);



    }

    public static long calc(long num) {
        long sum = 0;
        for (int i = 0; i < N; i++) {
            if (num < arr[i][0]) {
                continue;
            }

            sum += (Math.min(arr[i][1], num) - arr[i][0]) / arr[i][2] + 1;
        }
        return sum;
    }

}