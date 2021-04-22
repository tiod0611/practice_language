package main;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner input = new Scanner(System.in);

		while (true){
			int A = input.nextInt();
			int B = input.nextInt();
			
			if (A==0 && B==0) {
				input.close();
				break;				
			}
			System.out.println(A+B);
		}
	}

}
