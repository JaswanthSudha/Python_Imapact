public class leftRotateArray{
    public static void rotate(int arr[],int n,int k){
        if(n==0){
            return;
        }
        int temp[]=new int[k];
        for(int i=0;i<k;i++){
            temp[i]=arr[i];
        }
        for(int i=0;i<n-k;i++){
            arr[i]=arr[i+k];
        }
        for(int i=n-k;i<n;i++){
            arr[i]=temp[i-n+k];
        }

    }
    public static void main(String args[]){
        int arr[]={4,5,6,7,1,2,3};
        int k=3;
        int n=arr.length;
        rotate(arr,n,k);
        for(int i=0;i<n;i++){
            System.out.print(arr[i]+"->");
        }
    }
}