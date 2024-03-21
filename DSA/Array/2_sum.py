#two pointer technique
if __name__=="__main__":
    # array=list(map(int,input().split()))
    array=[2,7,11,15]
    target=9
    left=0
    right=len(array)-1
    sum1=0
    ans=[]
    while left<=right:
        sum1=array[left]+array[right]
        if sum1==target:
            ans.append(left)
            ans.append(right)
            # break
        if sum1>target:
            right-=1
        else:
            left+=1
        sum1=0 
    print(ans)

