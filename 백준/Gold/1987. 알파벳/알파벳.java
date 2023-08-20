import java.io.*;
import java.util.*;

public class Main {

    static int R, C, cnt, cntMax;
    static int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    static char[][] board;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        board = new char[R][C];
        visited = new boolean[26];

        for (int i = 0; i < R; i++) {
            String str = br.readLine();
            for (int j = 0; j < C; j++) {
                board[i][j] = str.charAt(j);
            }

        }

        cntMax = Integer.MIN_VALUE;
        dfs(0, 0, 1);
        System.out.println(cntMax);

    }

    private static void dfs(int x, int y, int cnt) {
        char inBoard = board[x][y];
        visited[inBoard - 65] = true;

        cntMax = Math.max(cnt, cntMax);

        for (int i = 0; i < 4; i++) {
            int nx = x + dir[i][0];
            int ny = y + dir[i][1];

            if (0 <= nx && nx < R && 0 <= ny && ny < C) {
                char inBoardN = board[nx][ny];
                if (!visited[inBoardN - 65]) {
                    dfs(nx, ny, cnt+1);
                    visited[inBoardN - 65] = false;
                }
            }
        }
    }
}