import java.util.Arrays;
import java.util.Scanner;

public class Galaga {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int TESTCASE = sc.nextInt();
		sc.nextLine();
		
		for(int i = 1; i < TESTCASE+1; i++) {
			String input = sc.nextLine();
			String[] input_str = input.split(" ");
			System.out.println("#"+ i +" "+getDayWin(Integer.parseInt(input_str[0]), Integer.parseInt(input_str[1]), 0));
			
		}
	}
	
	static int getDayWin(int playerA, int playerB, int day) {
		if (playerA < playerB) {
			return day;
		} else {
			return getDayWin(playerA * 2, playerB * 3, day+1);
		}
	}

}
