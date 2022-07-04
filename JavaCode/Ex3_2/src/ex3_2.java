import java.util.Arrays;
import java.util.Scanner;

public class ex3_2 {

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);
        int n, m, k;

        // n 배열 길이, m 더하는 횟수, k 반복 제한 횟수
        n = s.nextInt();
        m = s.nextInt();
        k = s.nextInt();

        int[] arr = new int[n];

        for(int i=0; i<n; i++)
            arr[i] = s.nextInt();

        Arrays.sort(arr);

        int first = arr[n-1];
        int second = arr[n-2];

        int res = 0;
        int count=0;

        for(int i=0; i<m; i++) {
            if(count == k) {
                res += second;
                count = 0;
            }
            else {
                res += first;
                count++;
            }
        }

        System.out.println(res);

    }
}
