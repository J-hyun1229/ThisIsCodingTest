package Chap8;

import java.math.BigInteger;

public class ex8_4 {

    static BigInteger[] d = new BigInteger[100];

    public static void main(String[] args) {
        d[1] = BigInteger.ONE;
        d[2] = BigInteger.ONE;
        int n = 99;

        fibo(n);

        for(int i=1; i<=99; i++)
            System.out.println(i + " : " + d[i]);
    }

    static void fibo(int n) {
        for(int i=3; i<=n; i++)
            d[i] = d[i-1].add(d[i-2]);

    }
}
