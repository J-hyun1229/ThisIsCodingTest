import java.util.Scanner;

public class ex3_4_sol {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int n,k;

        int res = 0;

        n = s.nextInt();
        k = s.nextInt();

        while(true) {
            int target = (n/k) * k;
            res += n-target;
            n = target;
            if(n<k)
                break;

            res += 1;
            n /= k;
        }

        res += (n-1);
        System.out.println(res);
    }
}
