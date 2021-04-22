package java_1330;

import java.util.Scanner;

public class Java_1330 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		
		int a = input.nextInt();
		int b = input.nextInt();
		input.close();
		
		if (a>b) {
			System.out.print(">");
		}else if(a<b) {
			System.out.print("<");
		}else {
			System.out.print("==");
		}
	}
}
