import java.util.*;
public class Day_3_sol {
    public static void main(String[] args) {
        Scanner a=new Scanner(System.in);
        System.out.print("Enter your name:");
        String s= a.nextLine();
        System.out.println("Original Name:"+s);
        String b=s.toUpperCase();
        String c="";
        for (int i =b.length()-1; i >=0; i--) {
            c=c+b.charAt(i);
        }
        System.out.println("Secret Code: "+c);
    }

}