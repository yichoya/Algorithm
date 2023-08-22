import java.io.*;
import java.util.*;

public class Main {

    static char[] vowel = {'a', 'e', 'i', 'o', 'u'};
    static char[] password, chars;
    static int L, C, cntVowel;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        L = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        chars = new char[C];

        String[] str = br.readLine().split(" ");
        for (int i = 0; i < str.length; i++) {
            chars[i] = str[i].charAt(0);
        }

        Arrays.sort(chars);

        password = new char[L];
        cntVowel = 0;

        comb(0, 0);
    }

    private static void comb(int cnt, int start) {
        if (cnt == L) {
            cntVowel = 0;
            for (char pw : password) {
                for (char vol : vowel) {
                    if (pw == vol) cntVowel++;
                }
            }

            if (1 <= cntVowel && cntVowel <= L - 2) {
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < L; i++) {
                    sb.append(password[i]);
                }
                System.out.println(sb);
            }
            return;
        }

        for (int i = start; i < C; i++) {
            password[cnt] = chars[i];
            comb(cnt + 1, i + 1);
        }
    }
}