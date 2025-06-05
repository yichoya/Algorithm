import java.io.*;
import java.util.*;

public class Main {
    // lowerBound: 처음 target 이상이 나오는 위치
    static int lowerBound(int[] arr, int target, int start) {
        int left = start, right = arr.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] < target)
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }

    // upperBound: 처음 target 초과가 나오는 위치
    static int upperBound(int[] arr, int target, int start) {
        int left = start, right = arr.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] <= target)
                left = mid + 1;
            else
                right = mid;
        }
        return left;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] A = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(A);
        long count = 0;

        // 이중 루프 + 이분탐색
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                int target = -(A[i] + A[j]);
                int low = lowerBound(A, target, j + 1);
                int high = upperBound(A, target, j + 1);
                count += (high - low);
            }
        }

        System.out.println(count);
    }
}
