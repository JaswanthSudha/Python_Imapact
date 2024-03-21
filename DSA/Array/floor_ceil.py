def floor(arr,left,right,x):
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]>x:
            right=mid-1
        if arr[mid]<=x:
            ans=mid
            left=mid+1
    return arr[ans]
def ceil(arr,left,right,x):
    ans=-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]<x:
            left=mid+1
        if arr[mid]==x:
            return arr[mid]
        if arr[mid]>x:
            ans=mid
            right=mid-1
    return arr[ans]
if __name__=="__main__":
    arr=list(map(int,input().split()))
    left=0
    n=len(arr)
    right=n-1
    x=2
    ans=floor(arr,left,right,x)
    ans2=ceil(arr,left,right,x)
    print(ans)
    print(ans2)

        