package MinMax;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Scanner scan = new Scanner(System.in);
	
		int length = scan.nextInt();	
		int[] arr = new int[length];
		for(int i=0; i<length; i++) {
			arr[i] = scan.nextInt();
		}
		scan.close();

		Arrays.sort(arr);
		System.out.println(arr[0]+" "+arr[length-1]);
		
	}

}
