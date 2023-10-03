import java.io.*;
import java.util.*;

public class Main {
    static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int R, C;
    static int[][] visited;
    static int[][] dir = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    static char[][] board;
    static Deque<Point> q;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        board = new char[R][C];
        visited = new int[R][C];
        q = new ArrayDeque<>();

        for (int i = 0; i < R; i++) {
            String tmp = br.readLine();
            for (int j = 0; j < C; j++) {
                visited[i][j] = -1;
                board[i][j] = tmp.charAt(j);

                if (board[i][j] == '*') {
                    q.offerFirst(new Point(i, j));
                    visited[i][j] = 0;
                }

                if (board[i][j] == 'S') {
                    q.offer(new Point(i, j));
                    visited[i][j] = 0;
                }
            }
        }

        String res = bfs();
        System.out.println(res);
    }

    static String bfs() {
        while (!q.isEmpty()) {
            Point cur = q.poll();
            int x = cur.x;
            int y = cur.y;

            for (int i = 0; i < 4; i++) {
                int dx = x + dir[i][0];
                int dy = y + dir[i][1];

                if (!(0 <= dx && dx < R && 0 <= dy && dy < C)) {
                    continue;
                }
                if (visited[dx][dy] != -1) {
                    continue;
                }
                if (board[dx][dy] == '*' || board[dx][dy] == 'X') {
                    continue;
                }

                if (board[dx][dy] == 'D' && board[x][y] == '*') {
                    continue;
                }
                if (board[dx][dy] == 'D' && board[x][y] == 'S') {
                    return Integer.toString(visited[x][y] + 1);
                }

                q.offer(new Point(dx, dy));
                board[dx][dy] = board[x][y];
                visited[dx][dy] = visited[x][y] + 1;
            }
        }

        return "KAKTUS";
    }
}