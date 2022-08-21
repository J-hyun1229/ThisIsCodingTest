package Chap8;

// 재귀호출과 메모이제이션을 이용한 피보나치 함수 코드
public class ex8_3 {

    static long[] d = new long[100]; // 0으로 초기화.

    public static void main(String[] args) {
        System.out.println(fibo(6));
    }

    static long fibo(int x) {
        System.out.print("f(" + x + ") ");
        if (x==1 || x==2) {
            return 1;
        }
        if (d[x] != 0) {
            return d[x];
        }
        d[x] = fibo(x-1) + fibo(x-2);
        return d[x];
    }
}
