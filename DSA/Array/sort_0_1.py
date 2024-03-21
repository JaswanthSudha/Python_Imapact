if __name__=="__main__":
    arr=[0,1,0,1,0]
    left=0
    right=len(arr)-1
    while left<right:
        if arr[left]==1 and arr[right]==0:
            arr[left],arr[right]=arr[right],arr[left]
        if arr[left]!=1:
            left+=1
        if arr[right]!=0:
            right-=1
    print(arr)
            
