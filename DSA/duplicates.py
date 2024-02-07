def function(arr,n):
    flag=False 
    ans=[]
    for i in range(len(arr)):
        if arr[i]!=-1:
            for j in range(i+1,len(arr)):
                if arr[i]==arr[j]:
                    arr[j]=-1
                    flag=True
        if flag==True:
            ans.append(arr[i])
            flag=False
    if len(ans)==0:
        return [-1]
    return sorted(ans)
def optimized_solution(arr,n):
    for item in arr:
        index=item%n
        arr[index]+=n
    print(arr)

arr=[2,3,1,1,2,3]
n=5
ans1=optimized_solution(arr,n)
print(ans1)




