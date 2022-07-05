import java.util.Scanner;

public class ex3_4 {

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);

        int n,k;

        n = s.nextInt();
        k = s.nextInt();

        int count = 0;

        while(true) {
            if(n == 1)
                break;

            if(n%k != 0) {
                n--;
                count++;
            }
            else {
                n /= k;
                count++;
            }

        }

        System.out.println(count);

    }
}
