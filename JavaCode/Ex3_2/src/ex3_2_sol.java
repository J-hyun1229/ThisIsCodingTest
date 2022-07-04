import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class ex3_2_sol {

    public static void main(String[] args)throws Exception {

        // BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Scanner s = new Scanner(System.in);

        int n, m, k;

        n = s.nextInt();
        m = s.nextInt();
        k = s.nextInt();

        int[] arr = new int[n];

        for(int i=0; i<n; i++)
            arr[i] = s.nextInt();

        Arrays.sort(arr);
        // 가장 큰 수가 더해지는 횟수와 두번째로 큰 수가 더해지는 횟수를 구한다.
        int first = arr[n-1];
        int second = arr[n-2];
        int firstCount = (m / (k+1)) * k + (m % (k+1));
        int secondCount = m - firstCount;

        int res = (first * firstCount) + (second * secondCount);

        System.out.println(res);

    } // main
}
