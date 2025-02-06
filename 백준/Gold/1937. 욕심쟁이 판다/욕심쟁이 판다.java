import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n;
	static int[][] board;
	static int cnt;
	static int[][] dp;
	static int[][] dxy = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		n = Integer.parseInt(br.readLine());

		board = new int[n][n];
		dp = new int[n][n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
				dp[i][j] = -1;
			}
		}

		cnt = -12345;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cnt = Math.max(cnt, recur(i, j));
			}
		}
		System.out.println(cnt);

	}
	public static int recur(int x, int y) {
		int tmp = 1;
		for (int i = 0; i < 4; i++) {
			int nx = x + dxy[i][0];
			int ny = y + dxy[i][1];

			if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
				continue;
			}

			if (board[nx][ny] > board[x][y]) {
				if (dp[nx][ny] != -1) {
					tmp = Math.max(tmp, dp[nx][ny] + 1);
				}
				else {
					tmp = Math.max(tmp, recur(nx, ny) + 1);
				}
			}

		}
		return dp[x][y] = tmp;
	}
}
