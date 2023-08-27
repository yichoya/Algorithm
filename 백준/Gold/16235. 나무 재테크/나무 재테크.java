import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static class Tree implements Comparable<Tree>{
        int age;
        boolean isDead;

        public Tree(int age, boolean isDead) {
            this.age = age;
            this.isDead = isDead;
        }

        @Override
        public int compareTo(Tree o) {
            return this.age - o.age;
        }
    }

    static ArrayList<Tree>[][] trees;
    static int[][] s2d2, foods;
    static int N, M, K, ans;
    static int[][] dir = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        trees = new ArrayList[N + 1][N + 1]; // 심어져있는 나무의 정보를 저장하는 배열
        s2d2 = new int[N + 1][N + 1]; // 로봇이 추가하는 양분의 양
        foods = new int[N + 1][N + 1]; // 양분의 값을 저장하는 배열

        for (int i = 1; i <= N ; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N ; j++) {
                trees[i][j] = new ArrayList<>();
                s2d2[i][j] = Integer.parseInt(st.nextToken());
                foods[i][j] = 5; // 초기 양분: 5
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int age = Integer.parseInt(st.nextToken());
            trees[x][y].add(new Tree(age, false));
        }

        for (int i = 1; i <= K ; i++) {
            spring();
            summer();
            fall();
            winter();
        }

        ans = 0;
        for (int i = 1; i <= N ; i++) {
            for (int j = 1; j <= N; j++) {
                if (trees[i][j] == null) continue;

                for (Tree t : trees[i][j]) {
                    if (!t.isDead) ans++;
                }
            }
        }

        System.out.println(ans);
    }

    static void spring() {
        for (int i = 1; i <= N ; i++) {
            for (int j = 1; j <= N; j++) {
                if (trees[i][j] == null) continue;

                Collections.sort(trees[i][j]); // 나이 기준 오름차순으로 정렬
                for (Tree t : trees[i][j]) {
                    if (foods[i][j] < t.age) {
                        t.isDead = true;
                        continue;
                    }
                    foods[i][j] -= t.age;
                    t.age++;
                }

            }
        }
    }

    static void summer() {
        for (int i = 1; i <= N ; i++) {
            for (int j = 1; j <= N; j++) {
                if (trees[i][j] == null) continue;

//                List<Tree> tmp = new ArrayList<>();
//                for (Tree t : trees[i][j]) {
//                    if (t.isDead) {
//                        foods[i][j] += (int)(t.age / 2);
//                        tmp.add(t);
//                    }
//                }
//                trees[i][j].remove(tmp);
                for (int k = trees[i][j].size() - 1; k >= 0; k--) {
                    Tree t = trees[i][j].get(k);
                    if (t.isDead) {
                        foods[i][j] += (int)(t.age / 2);
                        trees[i][j].remove(t);
                    }
                }
            }
        }
    }

    static void fall() {
        for (int i = 1; i <= N ; i++) {
            for (int j = 1; j <= N; j++) {
                if (trees[i][j] == null) continue;

                for (Tree t : trees[i][j]) {
                    if (t.age % 5 == 0) {
                        for (int k = 0; k < 8; k++) {
                            int nx = i + dir[k][0];
                            int ny = j + dir[k][1];

                            if (nx <= 0 || nx > N || ny <= 0 || ny > N) continue;
                            trees[nx][ny].add(new Tree(1, false));
                        }
                    }
                }
            }
        }
    }

    static void winter() {
        for (int i = 1; i <= N ; i++) {
            for (int j = 1; j <= N; j++) {
                foods[i][j] += s2d2[i][j];
            }
        }
    }
}
