/* 1. summary:
 *  - r * c 격자에서 첫번째 열은 주변 빵집의 가스관, 마지막 열은 원웅이의 빵집
 *  - 가스관과 빵집을 연결하는 파이프라인의 최대 개수를 구하라
 *  - 각 칸은 오른쪽, 오른쪽 위 대각선, 오른쪽 아래 대각선으로 연결할 수 있다
 *  - 각 칸을 지나는 파이프는 하나여야 한다
 * 2. strategy:
 *  - 열 기준 탐색 -> 이동할 수 있는 경로 확인
 *  - 마지막 열에 도착했다면 옳은 경로이므로 cnt++
 *  - 옳은 경로인지 아닌지 판단할 수 있는 flag가 필요함
 * 3. note:
 */

import java.util.*;
import java.io.*;

public class Main {

    static int R, C, cnt;
    static int[] dx = {-1, 0, 1}, dy = {1, 1, 1};
    static char[][] board;
    static boolean flag, visited[][];

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        board = new char[R][C];
        visited = new boolean[R][C];

        for (int i = 0; i < R; i++) {
            String str = br.readLine();
            for (int j = 0; j < C; j++) {
                board[i][j] = str.charAt(j);
            }
        }

        for (int x = 0; x < R; x++) {
            flag = false;
            setPipe(x, 0);
        }

        System.out.println(cnt);
    }

    private static void setPipe(int x, int y) {
        if (y == C-1) {  // 파이프 설치 가능
            flag = true;
            visited[x][y] = true;
            cnt++;
            return;
        }

        for (int i = 0; i < 3; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx && nx < R && 0 <= ny && ny < C && board[nx][ny] == '.') {
                if (visited[nx][ny]) continue;

                setPipe(nx, ny);

                if(!flag) { // 파이프 라인을 완성하지 못했을 경우
                    visited[x][y] = true;  // 틀린 경로로 못가게
                } else { // 완성했을 경우
                    visited[x][y] = true;  // 한번 갔던 길 못가게
                    return;
                }
            }
        }
    }

}