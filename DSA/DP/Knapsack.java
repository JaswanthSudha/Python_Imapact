public class Knapsack{
    public static int max1(int a,int b){
        if(a>b){
            return a;
        }
        return b;
    }
    public static void main(String args[]){
        int weights[]= {2,3,5};
        int profit[]={20,15,40};
        int capacity=8;
        int arr[][]=new int[10][10];
        for(int i=0;i<=weights.length;i++){
            for (int j=0;j<=capacity;j++){
                if(i==0 || j==0){
                    arr[i][j]=0;
                }
                else if(j<weights[i-1]){
                    arr[i][j]=arr[i-1][j];
                }
                else{
                    int max=max1(8,profit[i-1]+arr[i-1][j-weights[i-1]]);
                    arr[i][j]=max;

                }
            }
        }
        for(int i=0;i<=weights.length;i++){
          for(int j=0;j<=capacity;j++){
            System.out.print(arr[i][j]);
          }
          System.out.println();
        }
    }
}