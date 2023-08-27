import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] population;
    static boolean[] isSelected, visited;
    static List<ArrayList<Integer>> nodeInfo; // 지역 연결 정보를 담는 배열
    static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        N = Integer.parseInt(br.readLine());

        population = new int[N];
        nodeInfo = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            population[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int e = Integer.parseInt(st.nextToken());
            nodeInfo.add(new ArrayList<>());
            for (int j = 0; j < e; j++) {
                int nodeNo = Integer.parseInt(st.nextToken());
                nodeInfo.get(i).add(nodeNo - 1);
            }
        }

        isSelected = new boolean[N];
        subSet(0);
        if (ans == Integer.MAX_VALUE)
            ans = -1;
        System.out.println(ans);

    }

    static int count(List<Integer> a) { // a 선거구와 b 선거구의 인구 수 차이 계산
        int sumA = 0, sumB = 0;
        for (int i = 0; i < N; i++) {
            if (isSelected[i]) {
                sumA += population[i];
            } else sumB += population[i];
        }

        return Math.abs(sumA - sumB);
    }

    static boolean check(List<Integer> a) {  // 같은 선거구끼리 다 연결되어있는지 확인
        //List<ArrayList<Integer>> aList = Arrays.asList(a);  // ArrayList -> List 변환
        Queue<Integer> q = new ArrayDeque<>();
        visited = new boolean[N];
        int cntArea = 1;

        q.offer(a.get(0));
        visited[a.get(0)] = true;

        while(!q.isEmpty()) {
            int cur = q.poll();
            for (int i = 0; i < nodeInfo.get(cur).size(); i++) {
                int node = nodeInfo.get(cur).get(i);

                if (!visited[node] && a.contains(node)) {
                    q.offer(node);
                    visited[node] = true;
                    cntArea++;
                }
            }
        }

        if (cntArea == a.size()) return true;
        return false;
    }

    static void subSet(int cnt) {  // 부분집합으로 선거구 a, b 나누기
        if(cnt == N) {
            List<Integer> a = new ArrayList<>();
            List<Integer> b = new ArrayList<>();

            for (int i = 0; i < N; i++) {
                if (isSelected[i] ? a.add(i): b.add(i));
            }
            
            if (a.size() == 0 || b.size() == 0)  {
                return;
            }

            // a끼리 b끼리 다 연결되어있는지 확인하는 함수 호출
            if (check(a) && check(b)) {
                ans = Math.min(ans, count(a));
            }
            return;
        }

        isSelected[cnt] = true;
        subSet(cnt + 1);
        isSelected[cnt] = false;
        subSet(cnt + 1);
    }
}