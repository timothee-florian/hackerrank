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