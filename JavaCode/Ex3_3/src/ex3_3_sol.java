import java.util.Scanner;

public class ex3_3_sol {
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        int n,m;

        n = s.nextInt();
        m = s.nextInt();

        int res = -1;

        for(int i=0; i<n; i++) {
            int minVal = 10001;
            for(int j=0; j<m; j++) {
                int tmp = s.nextInt();
                minVal = Math.min(minVal, tmp);
            }
            res = Math.max(res, minVal);
        }

        System.out.println(res);

    } // main
}
