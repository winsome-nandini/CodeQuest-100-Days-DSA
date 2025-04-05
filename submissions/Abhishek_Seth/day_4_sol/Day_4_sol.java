import java.util.*;
public class Day_4_sol{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n,s=0,d;
        n=sc.nextInt();
        System.out.print("Sum of digits:");
        while(n!=0){
            d=n%10;
            s=s*10+d;
            n=n/10;
        }
        n=s;
        s=0;
        while(n!=0){
            d=n%10;
            s+=d;
            n=n/10;
            System.out.print(" "+d+" ");
            if(n==0){
                System.out.print("=");
            }
            else{
                System.out.print("+");
            }
        }
        System.out.print(" "+s);
    }
}