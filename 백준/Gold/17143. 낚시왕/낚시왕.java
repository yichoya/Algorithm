import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

/* 1. summary
 *  - 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합을 구하라
 *  - 낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다
 *  - 1초 동안 일어나는 일: 낚시왕이 오른쪽으로 한 칸 이동 -> 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다
 *  	 -> 잡은 상어는 격자판에서 사라진다 -> 상어가 이동한다
 *  - 상어는 주어진 속도로 이동하고, 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다
 *  - 상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있고 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다
 *  - 입력 받는 정보 중 d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다
 * 2. strategy
 *  -
 * 3. note
 */

public class Main {
    static class Shark {
        int x, y, speed, d, size;
        boolean isDead;

        public Shark(int x, int y, int speed, int d, int size, boolean isDead) {
            super();
            this.x = x;
            this.y = y;
            this.speed = speed;
            this.d = d;
            this.size = size;
            this.isDead = isDead;
        }
    }

    static int R, C;
    static int[][] dir = {{}, {-1, 0}, {1, 0}, {0, 1}, {0, -1}};
    static int[][] grid;
    static int total;
    static HashMap<Integer, Shark> map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        grid = new int[R + 1][C + 1];
        map = new HashMap<>(M);
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int speed = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int size = Integer.parseInt(st.nextToken());

            Shark shark = new Shark(x, y, speed, d, size, false);
            map.put(size, shark);
            grid[x][y] = size;
        }

        // 낚시꾼 이동
        total = 0;
        for (int i = 1; i <= C; i++) {
                // 낚시꾼이 있는 열에서 가장 땅에 가까운 물고기
            //System.out.println("낚시 전" + Arrays.deepToString(grid));
            for(int k = 1; k <= R; k++) {
                if (grid[k][i] != 0) {
                    // 상어 잡기
                    // 특정 값을 사이즈로 가지는 상어객체를 뽑아서 점수 계산
//                        Shark shark = map.get(grid[k][i]);
//                        for (Map.Entry<Integer, Shark> o : map.entrySet()) {
//                            Integer s = o.getKey();
//                            Shark sh = o.getValue();
//                            if (s.equals(grid[k][i])) {
//                                total += sh.size;
//                                sh = null;
//                            }
//                        }
                    int grab = grid[k][i];
                    Shark deadShark = map.get(grab);
                    deadShark.isDead = true;
                    total += grab;
                    grid[k][i] = 0;
                    break;
                }

            }
            // 상어이동
            grid = new int[R + 1][C + 1];
            for (Shark shark : map.values()) {
                move(shark);
                //System.out.println("move 완료");
            }
        }

        System.out.println(total);
    }

    static void move(Shark s) {
        if (s.isDead) return;

        int speed = s.speed;
        int nx = s.x;
        int ny = s.y;
        int direc = s.d;
        //System.out.println(nx + " " + ny);
        while(--speed >= 0) {
            nx += dir[direc][0];
            ny += dir[direc][1];

            if (nx <= 0) {
                nx += 2;
                direc = 2;
            } else if (nx > R) {
                nx -= 2;
                direc = 1;
            } else if (ny <= 0) {
                ny += 2;
                direc = 3;
            } else if (ny > C) {
                ny -= 2;
                direc = 4;
            }
        }
        //System.out.println(nx + " " + ny);
        if (grid[nx][ny] < s.size) {
            //잡아먹힌 상어 정보 지우기
            if (grid[nx][ny] != 0) {
                Shark deadShark = map.get(grid[nx][ny]);
                deadShark.isDead = true;
            }
            grid[nx][ny] = s.size;
            //grid[s.x][s.y] = 0;// 원래 위치에서 지우기
            s.x = nx;
            s.y = ny;
            s.d = direc;
        } else {
            s.isDead = true;
        }
        //
        // System.out.println("이동 후" + Arrays.deepToString(grid));
    }

}