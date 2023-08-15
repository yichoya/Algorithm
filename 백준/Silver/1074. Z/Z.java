import java.io.*;
import java.util.*;

public class Main {

	static int n,r,c;
	static int answer;
	static int size;
	
	public static void run(int x,int y,int length) {
		if(x==r && y==c) {
			System.out.println(answer);
			return;
		}
		if(x<=r && y<=c && x+length>r && y+length>c) {
			length /= 2;
			run(x,y,length);
			run(x,y+length,length);
			run(x+length,y,length);
			run(x+length,y+length,length);
		} else {
			answer += (length*length);
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		size = (int)Math.pow(2, n);
		run(0,0,size);
	}
}