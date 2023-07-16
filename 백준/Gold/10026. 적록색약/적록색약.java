import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
    static int N;
    static char[][] board;
    static boolean[][] visited;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int res1, res2;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine());
        board = new char[N][N];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = str.charAt(j);
            }
        }
        res1 = 0;
        res2 = 0;
        solve();
        sb.append(res1).append(" ").append(res2);

        System.out.println(sb);
    }

    private static void solve() {
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j]) {
                    continue;
                }
                search(i, j, board[i][j]);
                res1++;
            }
        }
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (visited[i][j]) {
                    continue;
                }
                search2(i, j, board[i][j]);
                res2++;
            }
        }

    }
    // 일반인
    private static void search(int r, int c, char flag) {
        visited[r][c] = true;

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{r, c});

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nr = cur[0] + dx[i];
                int nc = cur[1] + dy[i];

                if (nr >= 0 && nr < N && nc >= 0 && nc < N && !visited[nr][nc] && board[nr][nc] == flag) {
                    visited[nr][nc] = true;
                    queue.add(new int[]{nr, nc});
                }
            }
        }

    }

    private static void search2(int r, int c, char flag) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{r, c});
        visited[r][c] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();

            for (int i = 0; i < 4; i++) {
                int nr = cur[0] + dx[i];
                int nc = cur[1] + dy[i];

                if (nr >= 0 && nr < N && nc >= 0 && nc < N && !visited[nr][nc]) {
                    if (flag == 'B') {
                        if (board[nr][nc] == flag) {
                            visited[nr][nc] = true;
                            queue.add(new int[]{nr, nc});
                        }
                    } else {
                        if (board[nr][nc] == 'R' || board[nr][nc] == 'G') {
                            visited[nr][nc] = true;
                            queue.add(new int[]{nr, nc});
                        }
                    }
                }
            }
        }

    }

}