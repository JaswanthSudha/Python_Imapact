import java.util.*;
public class one{
    public static int recursion(int n,int arr[]){
       if(n==0 || n==1){
        return n;
       }
       if(arr[n]!=0){
        return arr[n];
       }
       arr[n]=recursion(n-1,arr)+recursion(n-2,arr);
       return arr[n];

}
public static void main(String args[]){
    int arr[]=new int[10];
    System.out.println(recursion(9,arr));
}
}