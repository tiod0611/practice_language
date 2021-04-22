package java_2739;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		
		int N = input.nextInt();
		input.close();
		
		for (int i = 1; i <10; i++) {
			System.out.println(N+" * "+i+" = "+i*N);
		}

	}

}
