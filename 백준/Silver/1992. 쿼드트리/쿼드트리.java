import java.io.*;
import java.util.*;

public class Main {

    static int[][] video;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        video = new int[N][N];
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < N; j++) {
                video[i][j] = str.charAt(j) - '0';
            }
        }

        StringBuilder sb = new StringBuilder();
        makeZip(0, 0, N, sb);
        System.out.println(sb);
    }

    private static void makeZip(int x, int y, int N, StringBuilder sb) {
        if (checkNum(x, y, N)) { // 숫자가 모두 같을 때
            sb.append(video[x][y]);
        } else {
            sb.append("(");
            int n = N / 2;

            makeZip(x, y, n, sb);
            makeZip(x, y + n, n, sb);
            makeZip(x + n, y, n, sb);
            makeZip(x + n, y + n, n, sb);
            // 재귀 다 돌고 ) 추가
            sb.append(")");
        }

    }

    private static boolean checkNum(int x, int y, int N) {
        int tmp = video[x][y];
        for (int i = x; i < x + N; i++) {
            for (int j = y; j < y + N; j++) {
                if (video[i][j] != tmp) return false;
            }
        }
        return true;
    }
}