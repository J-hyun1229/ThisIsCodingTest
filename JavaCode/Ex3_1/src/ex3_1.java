import java.util.Scanner;

public class ex3_1 {

    public static void main(String[] args) throws Exception {

        Scanner s = new Scanner(System.in);

        int money = s.nextInt();

        int coinArr[] = {500, 100, 50, 10};

        int res=0;

        for(int coin:coinArr) {
            res += money / coin;
            money %= coin;
        }


        System.out.println(res);

    }
}
