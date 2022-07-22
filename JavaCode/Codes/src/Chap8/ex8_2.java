package Chap8;

import java.math.BigInteger;
import java.util.Scanner;

public class ex8_2 {

    static long[] arr;

    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);

        int n = s.nextInt();
        arr = new long[n+1];

        long res = fibo_memoization(n);
        System.out.println(res);

    }

    // 메모이제이션 기법을 적용한 재귀적 피보나치 함수
    static long fibo_memoization(int x) {

        if(x == 1 || x == 2)
            return 1;

        if(arr[x] != 0)
            return arr[x];

        arr[x] = fibo_memoization(x-1) + fibo_memoization(x-2);
        return arr[x];

    }
}
