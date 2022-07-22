package Chap8;

import java.util.Scanner;

public class ex8_1 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        int n = s.nextInt();

        System.out.println(fibo(n));

    }

    // 재귀호출로 구현한 피보나치 함수. 인자로 전달되는 수가 커지면 연산횟수가 기하급수적으로 증가한다.
    // 연산횟수 증가의 주된 원인은 중복되는 연산이 많은 것. 메모이제이션 기법을 이용하면 실행시간을 획기적으로 줄일 수 있다.
    static int fibo(int x) {
        if(x==1 || x==2)
            return 1;

        return fibo(x-1) + fibo(x-2);
    }
}
