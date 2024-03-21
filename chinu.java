public class chinu{

    public static int function1(){
       int ans=function2(3,5);
       System.out.println(ans+4);
       return ans;
    }
    public static int function2(int a,int b){
        return a+b;

    }
    public static void main(String args[]){
        int var=function1();
        System.out.println(var);


    }
}