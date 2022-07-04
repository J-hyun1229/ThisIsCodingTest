import java.util.Arrays;
import java.util.Scanner;

public class ex3_3 {
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        int n,m; // 행, 열

        n = s.nextInt();
        m = s.nextInt();

        int[][] arr = new int[n][m];

        for(int i=0; i<n; i++) {
            for(int j=0; j<m; j++) {
                arr[i][j] = s.nextInt();
            }
        }

        for(int i=0; i<n; i++)
            Arrays.sort(arr[i]);

        int res = -1;
        int tmp;

        for(int i=0; i<n; i++) {
            tmp = arr[i][0];
            if(res < tmp)
                res = tmp;
        }

        System.out.println(res);

        /*
        for(int[] a:arr) {
            for(int i:a)
                System.out.print(i);
            System.out.println();
        }
        */

    }
}
