import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static List<Integer> list;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        list = new ArrayList<>();
        list.add(0);
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            if (list.get(list.size() - 1) < arr[i]) {
                list.add(arr[i]);
            } else {
                binarySearch(0, list.size() - 1, arr[i]);
            }
            //System.out.println(list);
        }


        System.out.println(list.size() - 1);
    }

    private static void binarySearch(int l, int r, int value) {
        int mid = 0;
        while (l < r) {
            mid = (l + r) / 2;
            int comp = list.get(mid);

            if (comp == value) {
                return;
            }

            if (value >= comp) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        list.set(r, value);
    }
}