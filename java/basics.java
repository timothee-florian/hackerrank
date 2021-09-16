// https://www.hackerrank.com/challenges/java-stdin-and-stdout-1/problem
// Input and print
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        scan.close();

        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
    }
}


// https://www.hackerrank.com/challenges/java-if-else/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
// if else
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        if (N % 2 == 1) {
            System.out.println("Weird");
        }
        else if (N <= 5) {
            System.out.println("Not Weird");
        }
        else if (N <= 20) {
            System.out.println("Weird");
        }
        else {
            System.out.println("Not Weird");
        }

        scanner.close();
    }
}


// https://www.hackerrank.com/challenges/java-stdin-stdout/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
// stdIn stdout
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int i = scan.nextInt();
        double d = scan.nextDouble();
        scan.nextLine();  // empty the rest of the line
        String s =  scan.nextLine();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}

// https://www.hackerrank.com/challenges/java-output-formatting/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
// String formating
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++){
                String s1=sc.next();
                int x=sc.nextInt();
                System.out.printf("%-14s %03d\n", s1, x);
            }
            System.out.println("================================");

    }
}



// https://www.hackerrank.com/challenges/java-loops-i/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen
// for loop
public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(bufferedReader.readLine().trim());
        
        for (int i = 1; i <= 10; i++) {
            System.out.printf("%d x %d = %d\n", N, i, N*i);
        }

        bufferedReader.close();
    }
}


// https://www.hackerrank.com/challenges/java-loops/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen
// insertion loop
import java.util.*;
import java.io.*;
import java.lang.Math;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int v = 1;
            for (int j = 0; j < n; j++) {
                a = a + b * v;
                System.out.printf("%d ", a);
                v = v * 2;
            }
            System.out.printf("\n");
        }
        in.close();
        
    }
}